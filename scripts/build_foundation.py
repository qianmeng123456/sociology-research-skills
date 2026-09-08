"""Build reviewed Codex entrypoints around pinned, unmodified upstream references."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build():
    import yaml
    specs = json.loads((ROOT / 'sources/foundation-specs.json').read_text(encoding='utf-8'))
    commit = (ROOT / 'sources/upstream-commit.txt').read_text(encoding='utf-8-sig').strip()
    paths = (ROOT / 'sources/selected-paths.txt').read_text(encoding='utf-8-sig').splitlines()
    upstream_paths = {p.split('/')[-1]: p for p in paths}
    manifest = []
    for name, spec in specs.items():
        original = ROOT / 'vendor/wentorai' / name / 'SKILL.md'
        target = ROOT / 'skills' / name
        (target / 'references').mkdir(parents=True, exist_ok=True)
        (target / 'references/upstream.md').write_bytes(original.read_bytes())
        (target / 'LICENSE.txt').write_bytes((ROOT / 'sources/LICENSE-wentorai.txt').read_bytes())
        source = f'https://github.com/wentorai/research-plugins/blob/{commit}/{upstream_paths[name]}/SKILL.md'
        front = yaml.safe_dump({'name': name, 'description': spec['description'], 'metadata': {'version': '0.1.0', 'upstream_commit': commit, 'adaptation': 'sociology-reviewed-entrypoint'}}, allow_unicode=True, sort_keys=False).strip()
        body = f"---\n{front}\n---\n\n# {spec['title']}\n\n{spec['purpose']}\n\n## 工作方式\n\n"
        body += '\n'.join(f'{i}. {step}' for i, step in enumerate(spec['steps'], 1))
        body += f"\n\n## 交付\n\n{spec['output']}\n\n## 方法修订与适用边界\n\n{spec['correction']}\n\n"
        body += ('保留原始数据和处理记录；缺少数据时交付设计或代码草稿，不能填写虚构的样本量、系数、引文或已经完成的检验。代码执行前核对用户文件、软件版本与官方接口，只报告实际运行结果。\n\n'
                 '## 来源与按需参考\n\n'
                 f'本入口是社会学适配版，基于 [Wentor AI 原版]({source}) 整理，原版按 MIT 许可保留。需要原始示例或更多方法背景时读取 [上游快照](references/upstream.md) 的相关章节。快照保留了尚未逐段修复的简化规则与示例；本入口的修订是使用条件，不应直接复制快照代码作为经过验证的分析。\n')
        if spec.get('sources'):
            body += '\n核对依据：\n\n' + '\n'.join(f'- [{s[0]}]({s[1]})' for s in spec['sources']) + '\n'
        (target / 'SKILL.md').write_text(body, encoding='utf-8')
        manifest.append({'name': name, 'kind': 'adapted-upstream', 'source': source, 'upstream_commit': commit, 'upstream_sha256': digest(original), 'entry_sha256': digest(target / 'SKILL.md'), 'license': 'MIT (upstream)', 'local_path': f'skills/{name}', 'correction': spec['correction']})
    (ROOT / 'sources/foundation-lock.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Built {len(manifest)} reviewed foundation skills')


if __name__ == '__main__':
    build()
