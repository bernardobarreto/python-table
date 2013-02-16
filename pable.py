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
        final = []
        for r in buffer:
            final.append(r.render())
        return '\n'.join(final)

    def cell_spacing(self):
        return self.cell_padding() + len(self.style.border_y)

    def cell_padding(self):
        return self.style.padding_left + self.style.padding_right

    def column_width(self, n):
        try: n = self.column_widths[n]
        except: n = 0
        return n

    def columns_width(self):
        last = 0
        for i in self.columns_widths: last += (i + len(self.style.border_y))
        return last

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

    def render(self):
        y = self.table.style.border_y
        lines_render = []
        for line in range(self.height()):
            cells_line_render = []
            for cell in self.cells:
                cells_line_render.append(cell.render(line))
            lines_render.append(y + y.join(cells_line_render) + y)
        return '\n'.join(lines_render)


from re import sub
class Cell(object):

    def __init__(self, **kwargs):
        self.value = kwargs['value']
        self.index = kwargs['index']
        self.table = kwargs['table']
        self.colspan = 1
        self.width = len(self.value)

    def lines(self):
        return self.value.split('\n')

    def render(self, line=0):
        left = " " * self.table.style.padding_left
        right = " " * self.table.style.padding_right
        try: line = self.lines()[line]
        except: line = ''
        #render_width = len(line) - len(self.escape(line)) + self.width()
        return "%s%s%s" % (left, line, right)

    def width(self):
        padding = (self.colspan - 1) * self.table.cell_spacing
        inner_width = 0
        for i in range(1, self.colspan+1):
            inner_width += self.table.column_width(self.index + i -1)
        return inner_width + padding

    def escape(self, line):
        line = sub(r'\x1b(\[|\(|\))[;?0-9]*[0-9A-Za-z]', '', line)
        line = sub(r'\x1b(\[|\(|\))[;?0-9]*[0-9A-Za-z]', '', line)
        return sub(r'(\x03|\x1a)/', '', line)


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

