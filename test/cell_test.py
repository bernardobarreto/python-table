import unittest
from pable import Table, Row, Cell, Separator, Style, InvalidOptionError

class CellTest(unittest.TestCase):

    def test_create(self):
        table = Table([['a']])
        cell = Cell(value='v', index=0, table=table)
        self.assertEqual(cell.value, 'v')
        self.assertEqual(cell.index, 0)
        self.assertEqual(cell.table, table)

    def test_render(self):
        table = Table([['a']])
        cell = Cell(value='v', index=0, table=table)
        self.assertEqual(cell.render(), ' v ')

    def test_render_with_multiline_content(self):
        table = Table([['foo\nbar']])
        cell = table.rows[0].cells[0]
        self.assertEqual(cell.render(0), ' foo ')
        self.assertEqual(cell.render(1), ' bar ')

    def test_default_alignment_left(self):
        table = Table([['a']])
        cell = Cell(value='v', index=0, table=table)
        self.assertEqual(cell.alignment, 'left')

    def test_should_allow_overriding_of_alignment(self):
        table = Table([['a']])
        cell = Cell(value='v', index=0, table=table)
        cell.alignment = 'center'
        self.assertEqual(cell.alignment, 'center')

    def test_only_accepts_some_options_for_alignment(self):
        table = Table([['a']])
        cell = Cell(value='v', index=0, table=table)
        cell.alignment = 'left'
        cell.alignment = 'center'
        cell.alignment = 'right'
        def foo(): cell.alignment = 'foo'
        self.assertRaises(InvalidOptionError, foo)

    def test_lines(self):
        table = Table([['a\nfoobar']])
        cell = table.rows[0].cells[0]
        self.assertEqual(cell.lines[0], 'a')
        self.assertEqual(cell.lines[1], 'foobar')

    def test_use_largest_value_for_multiline_content(self):
        table = Table([['a\nfoobar']])
        cell = table.rows[0].cells[0]
        self.assertEqual(cell.value, 'a\nfoobar')
        self.assertEqual(cell.value_for_column_width_recalc(), 'foobar')

    def test_allow_colorized_content(self):
        pass

    def test_render_padding_properly(self):
        pass

    def test_dont_ignore_pipe_characters(self):
        pass

if __name__ == '__main__':
    unittest.main()
