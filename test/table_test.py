import unittest
from pable import Table, Row, Cell, Separator, Style

class TableTest(unittest.TestCase):

    def test_render(self):
        t = Table([['one', '1'], ['two', '2']])
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

    def test_default_alignment_left(self):
        table = Table([['a']])
        cell = Cell(value='v', index=0, table=table)
        self.assertEqual(cell.alignment, 'left')


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

