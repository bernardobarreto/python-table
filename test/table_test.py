import unittest
from pable import Table, Row, Cell, Separator, Style


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
        cell = row.cells[0]
        self.assertEqual(row.cell_index, 2)
        self.assertEqual(len(row.cells), 1)
        self.assertEqual(cell.value, 'foo')
        self.assertEqual(cell.index, 1)
        self.assertEqual(cell.table, row.table)

class CellTest(unittest.TestCase):

    def test_create(self):
        table = Table([['a']])
        cell = Cell({ 'value': 'v', 'index': 0, 'table': table })
        self.assertEqual(cell.value, 'v')
        self.assertEqual(cell.index, 0)
        self.assertEqual(cell.table, table)

    def test_render(self):
        table = Table([['a']])
        cell = Cell({ 'value': 'v', 'index': 0, 'table': table })
        self.assertEqual(cell.render(), ' v ')


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

