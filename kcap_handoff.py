"""Render a structured, non-canonical KCAP handoff from a JSON record."""
import json
import sys
from pathlib import Path

FIELDS = ('title', 'objective', 'evidence', 'outcome', 'limitations', 'next_steps')


def render(record):
    if not isinstance(record, dict):
        raise ValueError('record must be an object')
    for key in FIELDS:
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise ValueError(f'{key} must be non-empty text')
    sections = [('Objective', 'objective'), ('Evidence', 'evidence'), ('Outcome', 'outcome'),
                ('Limitations', 'limitations'), ('Next steps', 'next_steps')]
    lines = [f'# KCAP handoff: {record["title"]}', '',
             'Status: PROPOSED — working handoff, not a verified or promoted memory.', '']
    for heading, key in sections:
        lines.extend((f'## {heading}', '', record[key], ''))
    return '\n'.join(lines)


def main(args):
    if len(args) != 1:
        print('Usage: python kcap_handoff.py record.json', file=sys.stderr)
        return 2
    try:
        record = json.loads(Path(args[0]).read_text(encoding='utf-8'))
        print(render(record))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f'Invalid handoff: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
