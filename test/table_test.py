import unittest
from pable import Table, Row, Cell, Separator, Style, InvalidOptionError

class TableTest(unittest.TestCase):

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


class RowTest(unittest.TestCase):

    def test_create(self):
        table = Table([['a']])
        row = table.rows[0]
        self.assertEqual(row.table, table)
        self.assertEqual(row.cell_index, 1)
        self.assertEqual(row.cells_values, ['a'])

    def test_add_cell(self):
        row = Table([['a']]).rows[0]
        row.add_cell('foo')
        cell = row.cells[1]
        self.assertEqual(row.cell_index, 2)
        self.assertEqual(len(row.cells), 2)
        self.assertEqual(cell.value, 'foo')
        self.assertEqual(cell.index, 1)
        self.assertEqual(cell.table, row.table)

    def test_render(self):
        row = Table([['one', '1']]).rows[0]
        self.assertEqual(row.render(), '| one | 1 |\n')


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

class SeparatorTest(unittest.TestCase):

    def test_separator_render_up(self):
        table = Table([['a', 'b']])
        render = Separator(table).render_up()
        self.assertEqual(render, '+---+---+\n')

    def test_separator_render_down(self):
        table = Table([['a', 'b']])
        render = Separator(table).render_down()
        self.assertEqual(render, '+---+---+')


class StyleTest(unittest.TestCase):

    def test_create_new_style(self):
        style = Style()
        self.assertEqual(style.border_x, '-')
        self.assertEqual(style.border_y, '|')
        self.assertEqual(style.border_i, '+')
        self.assertEqual(style.padding_left, 1)
        self.assertEqual(style.padding_right, 1)
        self.assertEqual(style.width, None)
        self.assertEqual(style.alignment, None)

if __name__ == '__main__':
    unittest.main()
