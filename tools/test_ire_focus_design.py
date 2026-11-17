"""Graph/preview regression tests. No game installation is required or simulated."""
import copy
import re
import sys
import unittest

sys.dont_write_bytecode = True
import ire_focus_design as design
from check_ire_1936 import clean_script


class DesignGraphTests(unittest.TestCase):
    def setUp(self):
        self.source = design.SOURCE.read_text(encoding='utf-8-sig')
        self.rows = design.read_design(self.source)

    def test_exact_ranges_and_counts(self):
        self.assertEqual(len(self.rows), 140)
        for branch, (_, count) in design.BRANCHES.items():
            self.assertEqual(sum(code.startswith(branch) for code in self.rows), count)

    def test_duplicate_node_rejected(self):
        line = next(line for line in self.source.splitlines() if line.startswith('| **P01**'))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            design.read_design(self.source + '\n' + line)

    def test_missing_node_rejected(self):
        with self.assertRaisesRegex(ValueError, 'node mismatch'):
            design.read_design('\n'.join(line for line in self.source.splitlines()
                                         if not line.startswith('| **P28**')))

    def test_unknown_parent_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows['P02']['parents'] = ['P99']
        with self.assertRaisesRegex(ValueError, 'Undefined node'):
            design.validate_graph(rows)

    def test_cycle_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows['P01']['parents'] = ['P02']
        with self.assertRaisesRegex(ValueError, 'cycle'):
            design.validate_graph(rows)

    def test_conflicting_ancestors_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows['P10']['parents'] = ['P09', 'P14']
        with self.assertRaisesRegex(ValueError, 'Unreachable'):
            design.validate_graph(rows)

    def test_asymmetric_exclusion_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows['P09']['exclusions'].remove('P14')
        with self.assertRaisesRegex(ValueError, 'Asymmetric'):
            design.validate_graph(rows)

    def test_military_common_programs_survive_both_routes(self):
        ancestry = design.validate_graph(self.rows)
        for code in ['M19', 'M23', 'M24', 'M28']:
            self.assertIn('M05', ancestry[code])
            self.assertNotIn('M09', ancestry[code])
            self.assertNotIn('M14', ancestry[code])

    def test_all_nine_political_entries_exclude_each_other(self):
        for code in design.GROUPS[0]:
            self.assertEqual(set(self.rows[code]['exclusions']), set(design.GROUPS[0]) - {code})
        for code in ['P10', 'P15', 'P20', 'P25']:
            self.assertEqual(self.rows[code]['exclusions'], [])

    def test_preview_positions_no_cycles_or_overlaps(self):
        resolved, visiting = {}, set()

        def resolve(code):
            self.assertNotIn(code, visiting)
            if code in resolved:
                return resolved[code]
            visiting.add(code)
            anchor, x, y = design.political_position(code)
            if anchor:
                ax, ay = resolve(anchor)
                x, y = x + ax, y + ay
            visiting.remove(code)
            resolved[code] = x, y
            return x, y

        for code in self.rows:
            if code.startswith('P'):
                resolve(code)
        self.assertEqual(len(set(resolved.values())), 28)
        self.assertEqual([resolved[c][0] for c in ['P09', 'P14', 'P19', 'P24']], [0, 8, 16, 24])

    def test_preview_exactly_28_nodes_and_no_dangling_refs(self):
        tree = design.outputs(self.rows)['common/national_focus/IRE_KLN_focus.txt'].decode()
        ids = re.findall(r'\bid\s*=\s*(IRE_KLN_focus_\w+)', tree)
        self.assertEqual(len(ids), 28)
        self.assertEqual(len(set(ids)), 28)
        refs = re.findall(r'(?:focus|relative_position_id)\s*=\s*(IRE_KLN_focus_\w+)', tree)
        self.assertTrue(set(refs) <= set(ids))
        clean_script(tree, 'political preview')
        self.assertNotRegex(tree, r'\b(?:add_ideas|add_political_power|set_politics|promote_character)\s*=')

    def test_preview_rule_default_off_and_tree_gated(self):
        output = design.outputs(self.rows)
        rule = output['common/game_rules/IRE_KLN_rules.txt'].decode()
        tree = output['common/national_focus/IRE_KLN_focus.txt'].decode()
        clean_script(rule, 'preview rule')
        self.assertRegex(rule, r'default\s*=\s*\{\s*name\s*=\s*DISABLED')
        self.assertIn('has_game_rule = { rule = IRE_KLN_rule_focus_preview option = ENABLED }', tree)

    def test_localisation_pairs_and_all_names(self):
        output = design.outputs(self.rows)
        languages = []
        for language in ['russian', 'english']:
            raw = output[f'localisation/{language}/IRE_KLN_focus_l_{language}.yml']
            self.assertTrue(raw.startswith(b'\xef\xbb\xbf'))
            lines = raw.decode('utf-8-sig').splitlines()
            self.assertEqual(lines[0], f'l_{language}:')
            keys = []
            for line in lines[1:]:
                match = re.fullmatch(r' (\w+):0 "[^"\n]+"', line)
                self.assertIsNotNone(match)
                keys.append(match[1])
            self.assertEqual(len(keys), len(set(keys)))
            languages.append(set(keys))
            for i in range(1, 29):
                identifier = design.focus_id(f'P{i:02}')
                self.assertIn(identifier, keys)
                self.assertIn(identifier + '_desc', keys)
        self.assertEqual(*languages)

    def test_generated_files_up_to_date(self):
        for name, content in design.outputs(self.rows).items():
            self.assertEqual((design.ROOT / name).read_bytes(), content, name)


if __name__ == '__main__':
    unittest.main()
