"""Install this project's reviewed skills; never replace unrelated/local edits."""
import argparse
import hashlib
import json
import os
import shutil
import stat
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_link(path):
    return path.is_symlink() or bool(getattr(path.lstat(), 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def tree_hashes(path):
    result = {}
    for p in sorted(path.rglob('*')):
        if '__pycache__' in p.parts or p.suffix == '.pyc':
            continue
        if is_link(p):
            raise ValueError(f'Links/reparse points are not supported: {p}')
        if p.is_file():
            result[p.relative_to(path).as_posix()] = file_hash(p)
    return result


def plan_install(source, dest, previous=None, allow_update=False):
    source, dest = source.resolve(), dest.absolute()
    for part in [dest, *dest.parents]:
        if part.exists() and is_link(part):
            raise ValueError(f'Destination ancestor is a link/reparse point: {part}')
    dest = dest.resolve()
    if source == dest or source in dest.parents or dest in source.parents:
        raise ValueError('Source and destination must be separate trees')
    previous = previous or {}
    old_entries = {e['name']: e for e in previous.get('skills', [])} if previous.get('destination') == str(dest) else {}
    plan = []
    for skill in sorted(source.iterdir()):
        if not skill.is_dir() or not (skill / 'SKILL.md').is_file():
            continue
        if is_link(skill):
            raise ValueError(f'Source skill is a link: {skill}')
        target = dest / skill.name
        if target.exists() and (is_link(target) or not target.is_dir()):
            raise ValueError(f'Unsafe destination: {target}')
        hashes = tree_hashes(skill)
        action = 'install'
        if target.exists():
            current = tree_hashes(target)
            if current == hashes:
                action = 'unchanged'
            elif allow_update and old_entries.get(skill.name, {}).get('files') == current:
                if not set(current).issubset(hashes):
                    raise ValueError(f'Update would remove files; manual review required: {skill.name}')
                action = 'update-managed'
            else:
                raise ValueError(f'Existing skill differs; no overwrite: {target}')
        plan.append({'name': skill.name, 'action': action, 'files': hashes})
    if not plan:
        raise ValueError('No skills to install')
    return plan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dest', type=Path, default=Path.home() / '.agents/skills')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--update-managed', action='store_true')
    parser.add_argument('--receipt', type=Path, default=ROOT / 'validation/installation.json')
    args = parser.parse_args()
    previous = json.loads(args.receipt.read_text(encoding='utf-8')) if args.receipt.exists() else None
    source, dest = ROOT / 'skills', args.dest.absolute()
    plan = plan_install(source, dest, previous, args.update_managed)
    # Check alternate personal skill root for the exact names; don't introduce aliases.
    other = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills'
    if other.resolve() != dest.resolve():
        collisions = [e['name'] for e in plan if (other / e['name'] / 'SKILL.md').exists()]
        if collisions:
            raise ValueError(f'Names already present in alternate Codex skill root: {collisions}')
    if args.apply:
        for entry in plan:
            if entry['action'] == 'unchanged':
                continue
            for relative in entry['files']:
                src, target = source / entry['name'] / relative, dest / entry['name'] / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, target)
        for entry in plan:
            if tree_hashes(dest / entry['name']) != entry['files']:
                raise RuntimeError(f'Installed bytes differ: {entry["name"]}')
        receipt = {'created_at': datetime.now(timezone.utc).isoformat(), 'destination': str(dest.resolve()), 'source': str(source), 'skills': plan, 'verified_bytes': True}
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'applied': args.apply, 'count': len(plan), 'destination': str(dest), 'actions': {e['name']: e['action'] for e in plan}}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
