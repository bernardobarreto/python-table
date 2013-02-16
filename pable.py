class Table(object):

    def __init__(self, options):
        self.add_rows(options['rows'])
        self.column_widths = []
        self.style = Style()

    def add_rows(self, array):
        self.rows = []
        for r in array:
            self.rows.append(Row(table=self, array=r))

    def render(self):
        separator = Separator(table=self)
        buffer = self.rows
        buffer.insert(0, separator)
        buffer.append(separator)
        import pdb; pdb.set_trace()

    def cell_spacing(self):
        self.cell_padding() + len(self.style.border_y)

    def cell_padding(self):
        self.style.padding_left + self.style.padding_right

    def column_width(self, n):
        try: n = self.column_widths[n]
        except: n = 0
        return n

    def columns_width(self):
        last = 0
        for i in self.columns_widths: last += (i + len(self.style.border_y))

    def columns_number(self):
        return max(len(c.cells) for c in self.headings_with_rows())

    def headings_with_rows(self):
        return self.rows #TODO: headings


class Row(object):

    def __init__(self, table, array=[]):
        self.table = table
        self.cell_index = 0
        self.cells = []
        for item in array: self.add_cell(item)

    def add_cell(self, item):
        options = { 'value': item, 'index': self.cell_index, 'table': self.table }
        self.cells.append(Cell(options))
        self.cell_index += 1

    def height(self):
        return max(str(c.value).count("\n") for c in self.cells) + 1


class Cell(object):

    def __init__(self, options):
        self.value = options['value']
        self.index = options['index']
        self.table = options['table']

    def lines(self):
        return self.value.split('\n')


class Separator(Row):
    def render(self):
        arr_x = []
        for i in range(self.table.columns_number()):
            arr_x.append(self.table.style.border_x * (self.table.column_width(i)
                + self.table.cell_padding()))
        border_i = self.table.style.border_i
        return border_i + border_i.join(arr_x) + border_i


class Style(object):

    def __init__(self):
        self.border_x = '-'
        self.border_y = '|'
        self.border_i = '+'
        self.padding_left = 1
        self.padding_right = 1
        self.width = None,
        self.alignment = None

