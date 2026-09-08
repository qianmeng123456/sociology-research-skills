"""Validate the small questionnaire schema; no claim about measurement validity."""
import argparse
import json
import math
from pathlib import Path


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def validate(doc):
    errors = []
    questions = doc.get('questions', [])
    if not questions:
        return ['questions must not be empty']
    ids = [q.get('id') for q in questions]
    variables = [q.get('variable') for q in questions]
    if any(not isinstance(x, str) or not x for x in ids + variables):
        return ['Every id and variable must be a nonempty string']
    if len(set(ids)) != len(ids):
        errors.append('Duplicate question id')
    if len(set(variables)) != len(variables):
        errors.append('Duplicate variable')
    if 'END' in ids:
        errors.append('END is reserved')
    by_id = {q['id']: q for q in questions}
    if doc.get('start') not in by_id:
        errors.append('Unknown start')
    graph = {}
    for q in questions:
        qid, kind = q['id'], q.get('type')
        missing = q.get('missing', {})
        if not isinstance(missing, dict):
            errors.append(f'{qid}: missing must map codes to reasons')
            missing = {}
        if any(not reason for reason in missing.values()):
            errors.append(f'{qid}: empty missing reason')
        options = q.get('options', {})
        if kind == 'single':
            if not isinstance(options, dict) or not options:
                errors.append(f'{qid}: single needs options')
                options = {}
            if set(options) & set(missing):
                errors.append(f'{qid}: valid and missing codes overlap')
        elif kind == 'integer':
            lo, hi = q.get('min'), q.get('max')
            if type(lo) is not int or type(hi) is not int or lo > hi:
                errors.append(f'{qid}: invalid integer range')
            else:
                for code in missing:
                    try:
                        if lo <= float(code) <= hi:
                            errors.append(f'{qid}: missing code inside valid range')
                    except ValueError:
                        pass
        elif kind != 'text':
            errors.append(f'{qid}: unsupported type')
        rules = q.get('next', {})
        if not isinstance(rules, dict) or not rules:
            errors.append(f'{qid}: missing next rules')
            rules = {}
        legal = set(options) | set(missing) if kind == 'single' else set(missing)
        if kind == 'single' and '*' not in rules and not legal.issubset(rules):
            errors.append(f'{qid}: uncovered response route')
        if kind in ('integer', 'text') and '*' not in rules:
            errors.append(f'{qid}: numeric/text route needs default')
        for code, target in rules.items():
            if kind == 'single' and code != '*' and code not in legal:
                errors.append(f'{qid}: route for unknown code {code}')
            if kind == 'text' and code != '*':
                errors.append(f'{qid}: text only supports default route')
            if kind == 'integer' and code != '*' and code not in missing:
                try:
                    v = int(code)
                    valid = str(v) == code and type(q.get('min')) is int and type(q.get('max')) is int and q['min'] <= v <= q['max']
                except ValueError:
                    valid = False
                if not valid:
                    errors.append(f'{qid}: route for unknown integer code {code}')
            if target != 'END' and target not in by_id:
                errors.append(f'{qid}: unknown destination {target}')
        graph[qid] = set(rules.values())
    visited, active = set(), set()

    def visit(qid):
        if qid == 'END' or qid not in by_id:
            return
        if qid in active:
            errors.append(f'Cycle at {qid}')
            return
        if qid in visited:
            return
        active.add(qid)
        visited.add(qid)
        for target in graph[qid]:
            visit(target)
        active.remove(qid)

    visit(doc.get('start'))
    for qid in set(ids) - visited:
        errors.append(f'Unreachable question {qid}')
    scale_ids = set()
    for scale in doc.get('scales', []):
        sid = scale.get('id')
        if not isinstance(sid, str) or not sid or sid in scale_ids:
            errors.append('Invalid or duplicate scale id')
        scale_ids.add(sid)
        items = scale.get('items', [])
        if not items or len(items) != len(set(items)) or any(i not in by_id for i in items):
            errors.append(f'{sid}: invalid scale items')
            continue
        minimum = scale.get('min_answered')
        if type(minimum) is not int or not 1 <= minimum <= len(items):
            errors.append(f'{sid}: invalid min_answered')
        lo, hi = scale.get('min'), scale.get('max')
        if not number(lo) or not number(hi) or lo >= hi:
            errors.append(f'{sid}: invalid scale range')
            continue
        if scale.get('method') not in ('mean', 'sum'):
            errors.append(f'{sid}: invalid scoring method')
        if not set(scale.get('reverse', [])).issubset(items):
            errors.append(f'{sid}: reverse item outside scale')
        for item in items:
            q = by_id[item]
            if q['type'] != 'single':
                errors.append(f'{sid}: scoring supports numeric single-choice items only')
                continue
            try:
                values = [float(k) for k in q['options']]
                if any(not math.isfinite(x) or not lo <= x <= hi for x in values):
                    errors.append(f'{sid}: item values outside scale range')
            except (ValueError, KeyError):
                errors.append(f'{sid}: nonnumeric scale codes')
    return sorted(set(errors))


def next_question(question, answer):
    code = str(answer)
    if question['type'] == 'single' and code not in question['options'] and code not in question.get('missing', {}):
        raise ValueError(f'Invalid answer for {question["id"]}')
    if question['type'] == 'integer' and code not in question.get('missing', {}):
        if type(answer) is not int or not question['min'] <= answer <= question['max']:
            raise ValueError(f'Invalid integer answer for {question["id"]}')
    if question['type'] == 'text' and not isinstance(answer, str):
        raise ValueError('Text answer must be a string')
    rules = question['next']
    return rules[code] if code in rules else rules['*']


def score_scale(doc, scale_id, answers):
    """Score only supplied valid item codes; caller must check eligibility separately."""
    if validate(doc):
        raise ValueError('Invalid questionnaire')
    scale = next(s for s in doc['scales'] if s['id'] == scale_id)
    by_id = {q['id']: q for q in doc['questions']}
    values = []
    for item in scale['items']:
        answer = answers.get(item)
        q = by_id[item]
        if answer is None or str(answer) in q.get('missing', {}):
            continue
        if isinstance(answer, bool) or str(answer) not in q['options']:
            raise ValueError(f'Invalid value for {item}: {answer!r}')
        value = float(answer)
        if item in scale.get('reverse', []):
            value = scale['min'] + scale['max'] - value
        values.append(value)
    if len(values) < scale['min_answered']:
        return None
    return sum(values) / len(values) if scale['method'] == 'mean' else sum(values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('questionnaire', type=Path)
    args = parser.parse_args()
    try:
        doc = json.loads(args.questionnaire.read_text(encoding='utf-8-sig'))
        errors = validate(doc)
    except (ValueError, TypeError, KeyError, AttributeError, OSError) as exc:
        errors = [f'Invalid document: {exc}']
    print(json.dumps({'ok': not errors, 'errors': errors, 'scope': 'structure and coding only; not validity, ethics, or platform deployment'}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
