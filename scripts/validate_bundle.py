"""Structural checks, source integrity and optional installed-byte verification."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from install_local import tree_hashes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--validator', type=Path, required=True)
    parser.add_argument('--installed', action='store_true')
    args = parser.parse_args()
    errors, checked = [], []
    names = set()
    for skill in sorted((ROOT / 'skills').iterdir()):
        if not (skill / 'SKILL.md').exists():
            continue
        run = subprocess.run([sys.executable, '-X', 'utf8', str(args.validator), str(skill)], capture_output=True, text=True, encoding='utf-8')
        if run.returncode:
            errors.append(f'{skill.name}: {run.stdout.strip()} {run.stderr.strip()}')
        entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
        match = re.search(r'^name: (.+)$', entry, re.M)
        name = match.group(1) if match else ''
        if not name or name in names or name != skill.name:
            errors.append(f'{skill.name}: name/directory mismatch or duplicate')
        names.add(name)
        for p in skill.rglob('*.md'):
            if p.name == 'upstream.md':
                continue  # historical source, not maintained local guidance
            for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                local = (p.parent / unquote(target.split('#')[0])).resolve()
                if not local.exists() or not local.is_relative_to(skill.resolve()):
                    errors.append(f'{p.relative_to(ROOT)}: unresolved/nonportable reference {target}')
        checked.append(skill.name)
    lock = json.loads((ROOT / 'sources/foundation-lock.json').read_text(encoding='utf-8'))
    for e in lock:
        raw = ROOT / 'vendor/wentorai' / e['name'] / 'SKILL.md'
        original = ROOT / 'skills' / e['name'] / 'references/upstream.md'
        if raw.read_bytes() != original.read_bytes() or hashlib.sha256(raw.read_bytes()).hexdigest() != e['upstream_sha256']:
            errors.append(f'{e["name"]}: upstream integrity mismatch')
        entry = ROOT / 'skills' / e['name'] / 'SKILL.md'
        if hashlib.sha256(entry.read_bytes()).hexdigest() != e['entry_sha256']:
            errors.append(f'{e["name"]}: entry differs from build lock')
        if not (entry.parent / 'LICENSE.txt').exists():
            errors.append(f'{e["name"]}: upstream license missing')
    if len(lock) != 20 or len(checked) != 27:
        errors.append(f'Expected 20 foundation and 27 total, found {len(lock)} and {len(checked)}')
    if args.installed:
        receipt = json.loads((ROOT / 'validation/installation.json').read_text(encoding='utf-8'))
        if {e['name'] for e in receipt['skills']} != names:
            errors.append('Receipt skill set differs from source')
        for e in receipt['skills']:
            src, installed = ROOT / 'skills' / e['name'], Path(receipt['destination']) / e['name']
            if not installed.is_dir() or tree_hashes(src) != tree_hashes(installed) or tree_hashes(installed) != e['files']:
                errors.append(f'{e["name"]}: source/install/receipt mismatch')
    report = {'ok': not errors, 'skill_count': len(checked), 'foundation_count': len(lock), 'custom_count': len(checked)-len(lock), 'checked': checked, 'errors': errors, 'installed_checked': args.installed, 'scope': 'structure, references, provenance hashes and installed bytes; not empirical research validity'}
    out = ROOT / 'validation/bundle.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k != 'checked'}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
