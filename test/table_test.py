import unittest
from pable import Table, Row, Cell, Separator, Style


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

