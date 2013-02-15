class Table(object):

    def __init__(self, options):
        self.rows = options['rows']
        self.column_widths = []


class Row(object):

    def __init__(self, array=[]):
        self.cell_index = 0
        self.cells = []
        for item in array:
            self.add_cell(item)

    def add_cell(self, item):
        options = { 'value': item, 'index': self.cell_index }
        self.cells.append(Cell(options))
        self.cell_index += 1

    def height(self):
        return max(str(c.value).count("\n") for c in self.cells) + 1


class Cell(object):

    def __init__(self, options):
        self.value = options['value']
        self.index = options['index']

    def lines(self):
        return self.value.split('\n')

