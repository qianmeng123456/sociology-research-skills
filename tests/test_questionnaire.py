import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('questionnaire', ROOT / 'skills/sociological-survey-design/scripts/check_questionnaire.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class QuestionnaireTests(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads((ROOT / 'examples/survey-demo/questionnaire.json').read_text(encoding='utf-8'))
        self.q = {q['id']: q for q in self.doc['questions']}

    def test_demo_paths(self):
        self.assertEqual(mod.validate(self.doc), [])
        self.assertEqual(mod.next_question(self.q['C0'], 0), 'END')
        self.assertEqual(mod.next_question(self.q['S1'], -99), 'END')
        for code in (0, -98, -99):
            self.assertEqual(mod.next_question(self.q['E1'], code), 'B1')
        self.assertEqual(mod.next_question(self.q['E1'], 1), 'E2')
        for code in (1, 30, -98, -99):
            self.assertEqual(mod.next_question(self.q['E2'], code), 'B1')

    def test_invalid_integer_boundary(self):
        for value in (0, 31, 1.5, True):
            with self.assertRaises(ValueError):
                mod.next_question(self.q['E2'], value)

    def test_missing_scores_never_zero(self):
        for method in ('mean', 'sum'):
            self.doc['scales'][0]['method'] = method
            for answers in ({}, {'B1': -99, 'B2': -98}, {'B1': 4, 'B2': 5}):
                self.assertIsNone(mod.score_scale(self.doc, 'belonging_candidate', answers))

    def test_score_and_reverse_with_zero_lower_bound(self):
        self.assertEqual(mod.score_scale(self.doc, 'belonging_candidate', {'B1': 1, 'B2': 3, 'B3': 5}), 3)
        scale = self.doc['scales'][0]
        scale.update(min=0, max=4, min_answered=2, reverse=['B1'])
        for item in scale['items']:
            self.q[item]['options'] = {str(i): str(i) for i in range(5)}
        self.assertEqual(mod.score_scale(self.doc, scale['id'], {'B1': 0, 'B2': 2, 'B3': -99}), 3)

    def test_bad_codes_rejected(self):
        for value in (9, True, 'unexpected'):
            with self.assertRaises(ValueError):
                mod.score_scale(self.doc, 'belonging_candidate', {'B1': value})

    def test_conflicting_codes(self):
        self.q['B1']['missing']['1'] = 'refusal'
        self.assertTrue(any('overlap' in e for e in mod.validate(self.doc)))

    def test_unknown_destination_and_cycle(self):
        self.q['F1']['next']['*'] = 'missing_id'
        self.assertTrue(any('destination' in e for e in mod.validate(self.doc)))
        self.q['F1']['next']['*'] = 'B1'
        self.assertTrue(any('Cycle' in e for e in mod.validate(self.doc)))

    def test_duplicate_and_missing_branch(self):
        self.q['B2']['variable'] = self.q['B1']['variable']
        del self.q['E1']['next']['-99']
        errors = mod.validate(self.doc)
        self.assertIn('Duplicate variable', errors)
        self.assertTrue(any('uncovered' in e for e in errors))

    def test_unreachable_question(self):
        self.q['E1']['next']['1'] = 'B1'
        self.assertIn('Unreachable question E2', mod.validate(self.doc))

    def test_invalid_scale_config(self):
        self.doc['scales'][0]['min_answered'] = 0
        self.assertTrue(any('min_answered' in e for e in mod.validate(self.doc)))


if __name__ == '__main__':
    unittest.main()
