import unittest
from pable import Table, Row, Cell, Separator, Style, InvalidOptionError

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

if __name__ == '__main__':
    unittest.main()
