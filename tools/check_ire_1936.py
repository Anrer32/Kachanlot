#!/usr/bin/env python3
"""Read-only checks for the stage-1 module; not a Clausewitz parser."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def clean_script(text, path):
    """Strip comments/strings while checking quotes and balanced blocks."""
    result = []
    depth = 0
    quote = comment = escape = False
    for char in text:
        if comment:
            comment = char != '\n'
            result.append('\n' if char == '\n' else ' ')
        elif quote:
            if escape:
                escape = False
            elif char == '\\':
                escape = True
            elif char == '"':
                quote = False
            result.append(' ')
        elif char == '#':
            comment = True
            result.append(' ')
        elif char == '"':
            quote = True
            result.append(' ')
        else:
            depth += (char == '{') - (char == '}')
            require(depth >= 0, f'{path}: unexpected closing brace')
            result.append(char)
    require(not quote and depth == 0, f'{path}: unterminated string/block')
    return ''.join(result)


def main():
    paths = ['common/ideas/IRE_KLN_ideas.txt',
             'common/scripted_effects/IRE_KLN_effects.txt',
             'common/on_actions/IRE_KLN_on_actions.txt']
    texts = [clean_script((ROOT / p).read_text(encoding='utf-8-sig'), p)
             for p in paths]
    ideas, effect, hook = texts
    definitions = re.findall(r'\b(IRE_KLN_idea_\w+)\s*=\s*\{', ideas)
    require(len(definitions) == len(set(definitions)) == 6,
            'Expected six distinct country spirits')
    require(re.search(r'ideas\s*=\s*\{\s*country\s*=\s*\{', ideas),
            'Spirits must be under ideas/country')
    assignment = re.search(r'add_ideas\s*=\s*\{([^{}]+)\}', effect)
    require(assignment is not None, 'Missing add_ideas assignment')
    assigned = assignment[1].split()
    require(len(assigned) == 6 and set(assigned) == set(definitions),
            'Assigned spirit IDs do not match definitions')
    effect_id = 'IRE_KLN_effect_initialize_spirits_1936'
    flag_id = 'IRE_KLN_flag_spirits_1936_initialized'
    require(re.search(rf'\b{effect_id}\s*=\s*yes', hook), 'Startup link missing')
    require(re.search(r'limit\s*=\s*\{\s*tag\s*=\s*IRE\s*\}', hook),
            'Startup country filter missing')
    require('on_startup' in hook and 'on_monthly' not in hook, 'Unexpected hook')
    for pattern in [r'tag\s*=\s*IRE', r'date\s*>\s*1935\.12\.31',
                    r'date\s*<\s*1936\.1\.2',
                    rf'NOT\s*=\s*\{{\s*has_country_flag\s*=\s*{flag_id}\s*\}}']:
        require(re.search(pattern, effect), f'Missing init guard: {pattern}')
    require(re.search(rf'set_country_flag\s*=\s*{flag_id}', effect),
            'Missing completion flag')
    # Search the whole local common tree for conflicting own definitions.
    for identifier in [*definitions, effect_id]:
        matches = []
        for path in (ROOT / 'common').rglob('*.txt'):
            pattern = rf'(?m)^\s*{identifier}\s*=\s*\{{'
            if re.search(pattern, path.read_text(encoding='utf-8-sig')):
                matches.append(path)
        require(len(matches) == 1, f'{identifier}: definition count {len(matches)}')
    existing = '\n'.join(p.read_text(encoding='utf-8-sig')
                         for p in (ROOT / 'common/ideas').glob('*.txt')
                         if p.name != 'IRE_KLN_ideas.txt')
    for body in re.findall(r'modifier\s*=\s*\{([^{}]+)\}', ideas):
        for modifier in re.findall(r'(\w+)\s*=', body):
            require(re.search(rf'\b{modifier}\s*=', existing),
                    f'No local modifier example: {modifier}')
    for picture in re.findall(r'picture\s*=\s*(\w+)', ideas):
        require(re.search(rf'picture\s*=\s*{picture}\b', existing),
                f'No local picture example: {picture}')
    for language in ['russian', 'english']:
        path = ROOT / f'localisation/{language}/IRE_KLN_start_l_{language}.yml'
        raw = path.read_bytes()
        require(raw.startswith(b'\xef\xbb\xbf'), f'{language}: missing BOM')
        lines = raw.decode('utf-8-sig').splitlines()
        require(lines[0] == f'l_{language}:', f'{language}: wrong header')
        keys = []
        for line in lines[1:]:
            match = re.fullmatch(r'\s+(\w+):0 "[^"\n]+"', line)
            require(match, f'{language}: invalid localisation line: {line}')
            keys.append(match[1])
        expected = set(definitions) | {key + '_desc' for key in definitions}
        require(len(keys) == 12 and set(keys) == expected,
                f'{language}: missing/duplicate localisation keys')
    print('PASS: 3 scripts structurally balanced; 6 unique spirit definitions')
    print('PASS: 6 assignment references, startup link, date/tag/flag guards')
    print('PASS: modifier/picture examples exist locally; RU/EN 12 keys each, BOM')
    print('UNVERIFIED: vanilla/DLC collisions, game syntax/scopes, GFX, runtime effects')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, UnicodeError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
