class Table(object):

    def __init__(self, options):
        self.add_rows(options['rows'])
        self.column_widths = []

    def add_rows(self, array):
        self.rows = []
        for r in array:
            self.rows.append(Row(r))

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


class Separator(Row):
    def render():
        pass


class Style(object):

    def __init__(self):
        self.defaults = {
            'border_x': '-', 'border_y': '|',
            'border_i': '+', 'padding_left': 1,
            'padding_right': 1, 'width': None,
            'alignment': None
        }
