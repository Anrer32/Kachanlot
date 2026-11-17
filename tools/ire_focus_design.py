#!/usr/bin/env python3
"""Read the approved design, validate its graph, and build the P01-P28 preview.

--write updates only the manifest, political preview, rule and its localisation.
Default mode validates design + generated files without modifying them.
This is not a HoI4 parser or a runtime government-transition test.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import io
import itertools
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/ireland/focus_tree_design.md'
BRANCHES = {'P': ('politics', 28), 'E': ('economy', 28),
            'M': ('military', 28), 'D': ('diplomacy', 26),
            'A': ('alternate_history', 30)}
GROUPS = [['P09', 'P14', 'P19', 'P24', 'A01', 'A07', 'A13', 'A19', 'A25'],
          ['E09', 'E14'], ['E19', 'E24'], ['M09', 'M14'],
          ['D07', 'D12', 'D17', 'D22']]
ENGLISH = [
    'Unfinished Independence', 'Legacy of the War of Independence',
    'Legacy of the Civil War', 'The Eighth Dáil', 'The Fianna Fáil Mandate',
    'Debating the Republican Future', 'Public Order', 'The Future of Irish Democracy',
    'Continue de Valera’s Course', 'Limit the Influence of the Crown',
    'Draft a New Constitution', 'A Referendum on the Future of the State',
    'Sovereign Ireland', 'The Return of Constitutional Opposition',
    'The Cosgrave Legacy', 'A Coalition of Owners and Farmers',
    'Reconsider the Economic Confrontation', 'Constitutional Government',
    'The Voice of Labour', 'A National Labour Agreement',
    'Extend Social Guarantees', 'Representation for Working People',
    'A Social Republic', 'Above Party Differences', 'An All-Ireland Defence Committee',
    'Reconciliation of Veterans', 'Emergency Powers of Parliament', 'National Concord',
]


def focus_id(code):
    return 'IRE_KLN_focus_' + code


def read_design(text):
    rows = {}
    for line in text.splitlines():
        match = re.match(r'^\| \*\*([PEMDA]\d{2})\*\* \| (.*?) \| (.*?) \| (.*?) \|$', line)
        if not match:
            continue
        code, title, requirement, effect = match.groups()
        if code in rows:
            raise ValueError(f'Duplicate design node: {code}')
        parents = re.findall(r'\b[PEMDA]\d{2}\b', requirement)
        # The approved revision has one parent per non-root node. Do not infer
        # AND/OR semantics silently if a later design changes this convention.
        if len(parents) > 1:
            raise ValueError(f'{code}: multiple parents require an explicit AND/OR specification')
        if not parents and not requirement.startswith('Нет'):
            raise ValueError(f'{code}: unrecognised prerequisite specification: {requirement}')
        rows[code] = dict(title=title, parents=parents, requirement=requirement,
                          effect=effect, exclusions=[])
    expected = {f'{b}{i:02}' for b, (_, n) in BRANCHES.items() for i in range(1, n + 1)}
    if set(rows) != expected:
        raise ValueError(f'Design node mismatch: missing={expected-set(rows)}, extra={set(rows)-expected}')
    for group in GROUPS:
        for a, b in itertools.permutations(group, 2):
            rows[a]['exclusions'].append(b)
    validate_graph(rows)
    return rows


def validate_graph(rows):
    done, visiting, ancestors = set(), set(), {}

    def visit(code):
        if code not in rows:
            raise ValueError(f'Undefined node: {code}')
        if code in visiting:
            raise ValueError(f'Prerequisite cycle at {code}')
        if code in done:
            return ancestors[code]
        visiting.add(code)
        seen = {code}
        for parent in rows[code]['parents']:
            seen |= visit(parent)
        for item in seen:
            for excluded in rows[item]['exclusions']:
                if excluded not in rows:
                    raise ValueError(f'Undefined exclusion: {excluded}')
                if item not in rows[excluded]['exclusions']:
                    raise ValueError(f'Asymmetric exclusion: {item}/{excluded}')
                if excluded in seen:
                    raise ValueError(f'Unreachable node {code}: needs excluded {item}/{excluded}')
        visiting.remove(code)
        done.add(code)
        ancestors[code] = seen
        return seen

    for code in rows:
        visit(code)
    return ancestors


def political_position(code):
    number = int(code[1:])
    if number == 1:
        return '', 12, 0
    if number <= 8:
        return f'P{number-1:02}', 0, 1
    route, step = divmod(number - 9, 5)
    return ('P08', -12 + route * 8, 2) if step == 0 else (f'P{number-1:02}', 0, 1)


def outputs(rows):
    fields = ['code', 'planned_id', 'direction', 'title_ru', 'title_en', 'design_note',
              'prerequisite_groups', 'mutually_exclusive', 'available', 'bypass',
              'relative_position_id', 'x', 'y', 'cost', 'icon', 'effect_spec',
              'effect_status', 'design_status']
    data = io.StringIO(newline='')
    writer = csv.DictWriter(data, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for code, node in rows.items():
        row = dict.fromkeys(fields, '')
        row.update(code=code, planned_id=focus_id(code), direction=BRANCHES[code[0]][0],
                   title_ru=node['title'], design_note=node['requirement'],
                   prerequisite_groups=json.dumps([[focus_id(p)] for p in node['parents']]),
                   mutually_exclusive=json.dumps([focus_id(p) for p in node['exclusions']]),
                   effect_spec=node['effect'], effect_status='deferred',
                   design_status='approved_concept_graph_checked')
        if code.startswith('P'):
            anchor, x, y = political_position(code)
            row.update(title_en=ENGLISH[int(code[1:])-1],
                       available='preview only; mandate/government implementation deferred',
                       bypass='always = no', relative_position_id=focus_id(anchor) if anchor else '',
                       x=x, y=y, cost=3 if int(code[1:]) <= 8 else 5,
                       icon='GFX_goal_generic_political_pressure')
        writer.writerow(row)

    tree = [
        '# GENERATED by tools/ire_focus_design.py --write. Political PREVIEW only.',
        '# No mandates, laws, government changes or rewards are implemented here.',
        'focus_tree = {', '    id = IRE_KLN_tree_main', '    country = {',
        '        factor = 0', '        modifier = {', '            add = 100',
        '            tag = IRE',
        '            has_game_rule = { rule = IRE_KLN_rule_focus_preview option = ENABLED }',
        '        }', '    }', '    default = no',
        '    continuous_focus_position = { x = 500 y = 1800 }',
    ]
    for code, node in rows.items():
        if not code.startswith('P'):
            continue
        anchor, x, y = political_position(code)
        tree += ['    focus = {', f'        id = {focus_id(code)}',
                 '        icon = GFX_goal_generic_political_pressure',
                 f'        x = {x}', f'        y = {y}',
                 f'        cost = {3 if int(code[1:]) <= 8 else 5}']
        if anchor:
            tree.append(f'        relative_position_id = {focus_id(anchor)}')
        for parent in node['parents']:
            tree.append(f'        prerequisite = {{ focus = {focus_id(parent)} }}')
        # Alternative branches do not exist yet: do not create dangling focus refs.
        exclusions = [p for p in node['exclusions'] if p.startswith('P')]
        if exclusions:
            tree.append('        mutually_exclusive = { ' + ' '.join(f'focus = {focus_id(p)}' for p in exclusions) + ' }')
        tree += ['        available = { always = yes }',
                 '        bypass = { always = no }', '        cancel_if_invalid = yes',
                 '        continue_if_invalid = no',
                 '        completion_reward = { custom_effect_tooltip = IRE_KLN_tt_focus_preview }',
                 '        ai_will_do = {', '            factor = 1']
        if code in ['P09', 'P14', 'P19', 'P24']:
            tree += ['            modifier = {',
                     f'                factor = {100 if code == "P09" else 0}',
                     '                is_historical_focus_on = yes', '            }']
        tree += ['        }', '    }']
    tree += ['}']
    rule = '''# Opt-in inspection only. Default gameplay keeps the existing IRE tree.
IRE_KLN_rule_focus_preview = {
    name = IRE_KLN_rule_focus_preview
    group = IRE_KLN_rule_group
    default = {
        name = DISABLED
        text = IRE_KLN_preview_disabled
        desc = IRE_KLN_preview_disabled_desc
    }
    option = {
        name = ENABLED
        text = IRE_KLN_preview_enabled
        desc = IRE_KLN_preview_enabled_desc
    }
}
'''
    result = {
        'docs/ireland/FOCUS_140_MANIFEST.csv': data.getvalue().encode(),
        'common/national_focus/IRE_KLN_focus.txt': ('\n'.join(tree) + '\n').encode(),
        'common/game_rules/IRE_KLN_rules.txt': rule.encode(),
    }
    for language in ['russian', 'english']:
        ru = language == 'russian'
        strings = {
            'IRE_KLN_rule_group': 'Ирландия: разработка' if ru else 'Ireland: development',
            'IRE_KLN_rule_focus_preview': 'Предпросмотр политического каркаса' if ru else 'Political skeleton preview',
            'IRE_KLN_preview_disabled': 'Выключен' if ru else 'Disabled',
            'IRE_KLN_preview_disabled_desc': 'Сохранить действующее дерево IRE.' if ru else 'Keep the existing IRE focus tree.',
            'IRE_KLN_preview_enabled': 'Технический предпросмотр P01–P28' if ru else 'Technical P01–P28 preview',
            'IRE_KLN_preview_enabled_desc': 'Только граф и тексты. Правительства, законы и награды пока не реализованы.' if ru else 'Graph and text only. Governments, laws and rewards are not implemented.',
            'IRE_KLN_tt_focus_preview': 'Технический каркас: описанное действие ещё не реализовано. Фокус не выдаёт наград.' if ru else 'Technical skeleton: the described action is not implemented. This focus grants no rewards.',
        }
        for code, node in rows.items():
            if not code.startswith('P'):
                continue
            identifier = focus_id(code)
            strings[identifier] = node['title'] if ru else ENGLISH[int(code[1:])-1]
            strings[identifier + '_desc'] = (
                node['effect'] + ' Технический предпросмотр: эффект пока не реализован.' if ru else
                'Technical preview of the approved political route. The intended action is not implemented; see the design document. This focus grants no rewards.')
        text = '\n'.join([f'l_{language}:'] + [f' {key}:0 "{value}"' for key, value in strings.items()]) + '\n'
        result[f'localisation/{language}/IRE_KLN_focus_l_{language}.yml'] = text.encode('utf-8-sig')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    source = SOURCE.read_text(encoding='utf-8-sig')
    rows = read_design(source)
    # Require the exact reviewed group declarations; a changed concept must be
    # reviewed, not silently compiled using stale hard-coded exclusion groups.
    required = ['`E09` против `E14`', '`E19` против `E24`', '`M09` против `M14`',
                '`D07` / `D12` / `D17` / `D22`', '`A01`, `A07`, `A13`, `A19`, `A25`',
                '`P09`, `P14`, `P19`, `P24`']
    for declaration in required:
        if declaration not in source:
            raise ValueError(f'Review exclusion declaration: {declaration}')
    for path, content in outputs(rows).items():
        target = ROOT / path
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        elif not target.exists() or target.read_bytes() != content:
            raise ValueError(f'Generated file differs from approved source: {path}')
    print('PASS: exact approved 140 names/IDs and parent references; counts 28/28/28/26/30')
    print('PASS: no prerequisite cycles or ancestor/exclusion contradictions; symmetric groups')
    print('PASS: political preview and RU/EN outputs match the source; source SHA256:',
          hashlib.sha256(SOURCE.read_bytes()).hexdigest())
    print('NOT VALIDATED: mandate conditions, government transitions, HoI4 runtime or layout')


if __name__ == '__main__':
    main()
