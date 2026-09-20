import unittest
from pathlib import Path

from normalize_metadata import normalize_lines, parse_frontmatter


class PublicationMetadataTests(unittest.TestCase):
    def test_explicit_metadata_is_authoritative(self):
        lines = [
            'title: "Beyond Independent Genes"',
            'author: "A, <b>Zongxin Yang</b>*, B"',
            'author_role: "Co-first Author"',
            'venue: "ICML 2026"',
            'topic: "Translational Biomedical AI"',
            'pub_year: 2026',
            'pub_ym: 202607',
            'selected: true',
        ]
        self.assertEqual(normalize_lines('1047.md', lines), lines)

    def test_missing_metadata_is_still_inferred(self):
        lines = ['title: "Clinical model"', 'author: "Zongxin Yang, B"', 'venue: "2026"']
        result = normalize_lines('new.md', lines)
        for expected in ['author_role: "First Author"', 'topic: "Translational Biomedical AI"',
                         'pub_year: 2026', 'selected: false']:
            self.assertIn(expected, result)
        self.assertEqual(normalize_lines('new.md', result), result)

    def test_current_curated_publications_are_not_rewritten(self):
        root = Path(__file__).resolve().parents[2] / '_publications'
        for path in sorted(root.glob('*.md')):
            with self.subTest(path=path.name):
                _, lines, _ = parse_frontmatter(path.read_text())
                self.assertEqual(normalize_lines(path.name, lines), lines)


if __name__ == '__main__':
    unittest.main()
