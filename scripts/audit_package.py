"""Check artifact presence only; does not certify research or video quality."""
import argparse
import json
from pathlib import Path

REQUIRED = (
    'mother_md mother_txt storyboard research prompts delivery copy design '
    'concept cover cover_verification master share srt narration composition manifest voice '
    'voice_alignment mix verification share_verification snapshots'
).split()


def audit(root):
    root = Path(root).resolve()
    errors = []
    try:
        data = json.loads((root / 'project.json').read_text(encoding='utf-8-sig'))
    except (OSError, ValueError) as exc:
        return {'scope': 'artifact_presence_only', 'pass': False, 'errors': [str(exc)]}
    if not isinstance(data, dict):
        return {'scope': 'artifact_presence_only', 'pass': False, 'errors': ['project must be an object']}
    for key in ('title', 'short_title', 'duration_seconds', 'width', 'height', 'fps', 'status'):
        if not data.get(key):
            errors.append('missing project field: ' + key)
    items = data.get('deliverables', {})
    if not isinstance(items, dict):
        items = {}
        errors.append('deliverables must be an object')
    for key in REQUIRED:
        value = items.get(key)
        if not isinstance(value, str) or not value:
            errors.append('missing deliverable mapping: ' + key)
            continue
        path = (root / value).resolve()
        if not path.is_relative_to(root):
            errors.append('path escapes project: ' + key)
        elif key == 'snapshots':
            if not path.is_dir() or not any(p.is_file() and p.stat().st_size for p in path.rglob('*')):
                errors.append('missing or empty snapshots directory')
        elif not path.is_file() or path.stat().st_size == 0:
            errors.append('missing or empty file: ' + key + ': ' + value)
    return {'scope': 'artifact_presence_only', 'title': data.get('title'),
            'pass': not errors, 'errors': errors,
            'note': 'Research, media decoding, timing, identity and visual/audio review require separate verification.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project')
    args = parser.parse_args()
    report = audit(args.project)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['pass'] else 1)
