import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install_local.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class InstallTests(unittest.TestCase):
    def test_conflict_no_overwrite_and_managed_update(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, dest = root / 'source', root / 'dest'
            (source / 'sample').mkdir(parents=True)
            (source / 'sample/SKILL.md').write_text('v1')
            self.assertEqual(mod.plan_install(source, dest)[0]['action'], 'install')
            (dest / 'sample').mkdir(parents=True)
            (dest / 'sample/SKILL.md').write_text('v1')
            self.assertEqual(mod.plan_install(source, dest)[0]['action'], 'unchanged')
            receipt = {'destination': str(dest.resolve()), 'skills': [{'name':'sample', 'files':mod.tree_hashes(dest / 'sample')}]}
            (source / 'sample/SKILL.md').write_text('v2')
            with self.assertRaises(ValueError):
                mod.plan_install(source, dest)
            self.assertEqual(mod.plan_install(source, dest, receipt, True)[0]['action'], 'update-managed')
            (dest / 'sample/SKILL.md').write_text('user edit')
            with self.assertRaises(ValueError):
                mod.plan_install(source, dest, receipt, True)
            self.assertEqual((dest / 'sample/SKILL.md').read_text(), 'user edit')

    def test_nested_destination_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'source'
            source.mkdir()
            with self.assertRaises(ValueError):
                mod.plan_install(source, source / 'installed')


if __name__ == '__main__':
    unittest.main()
