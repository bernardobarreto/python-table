import unittest
from pable import Table, Row, Cell, Separator, Style, InvalidOptionError

class SeparatorTest(unittest.TestCase):

    def test_separator_render_up(self):
        table = Table([['a', 'b']])
        render = Separator(table).render_up()
        self.assertEqual(render, '+---+---+\n')

    def test_separator_render_down(self):
        table = Table([['a', 'b']])
        render = Separator(table).render_down()
        self.assertEqual(render, '+---+---+')

if __name__ == '__main__':
    unittest.main()
