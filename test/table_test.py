import unittest
from pable import Table, Row, Cell, Separator, Style


class CellTest(unittest.TestCase):

    def test_create(self):
        table = Table([['a']])
        cell = Cell({ 'value': 'v', 'index': 0, 'table': table })
        self.assertEqual(cell.value, 'v')
        self.assertEqual(cell.index, 0)
        self.assertEqual(cell.table, table)
        self.assertEqual(cell.colspan, 1)
        self.assertEqual(cell.width, 1)

    def test_render(self):
        table = Table([['a']])
        cell = Cell({ 'value': 'v', 'index': 0, 'table': table })
        self.assertEqual(cell.render(), ' v ')


class SeparatorTest(unittest.TestCase):

    def test_separator_render(self):
        table = Table([['a', 'b']])
        render = Separator(table).render()
        self.assertEqual(render, '+--+--+')


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

