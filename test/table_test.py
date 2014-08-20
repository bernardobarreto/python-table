import unittest
from pable import Table, Row, Cell, Separator, Style, InvalidOptionError

class TableTest(unittest.TestCase):

    def test_select_column(self):
        t = Table([['one', '1'], ['two', '2']])
        self.assertEqual(t.column(1), ['1', '2'])

    def test_number_of_columns(self):
        t = Table([['one', '1'], ['two', '2', '3']])
        self.assertEqual(t.number_of_columns(), 3)

    def test_columns(self):
        t = Table([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(t.columns(), [['1', '4'], ['2', '5'], ['3', '6']])

    def test_column_length(self):
        t = Table([['one', '1'], ['three', '2', '3']])
        self.assertEqual(t.column_length(1), 5)

    def test_render(self):
        t = Table([['one', '1'], ['two', '2']])
        out = """+-----+---+
| one | 1 |
| two | 2 |
+-----+---+"""
        self.assertEqual(t.render(), out)

    def test_break_multiline_content(self):
        t = Table([['one\none', '1'], ['two', '2']])
        out = """+-----+---+
| one | 1 |
| two | 2 |
+-----+---+"""
        self.assertEqual(t.render(), out)

    def test_accepts_differents_types_of_cell_values(self):
        t = Table([['one', 1], ['two', 1.2]])
        out = """+-----+-----+
| one | 1   |
| two | 1.2 |
+-----+-----+"""

        self.assertEqual(t.render(), out)

    def test_max_columns_widths(self):
        t = Table([['one', '1'], ['two', '2']])
        self.assertEqual(t.max_columns_widths, [3, 1])

    def test_cell_spacing(self):
        t = Table([['one', '1'], ['two', '2']])
        self.assertEqual(t.cell_spacing, 3)

    def test_cell_padding(self):
        t = Table([['one', '1'], ['two', '2']])
        self.assertEqual(t.cell_spacing, 3)

if __name__ == '__main__':
    unittest.main()
