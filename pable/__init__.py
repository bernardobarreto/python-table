class Table(object):

    def __init__(self, rows):
        self.rows_values = [[str(value) for value in row] for row in rows] # convert to str
        self.add_rows(self.rows_values)
        self.style = Style()

    def add_rows(self, array):
        self.rows = []
        for r in array: self.rows.append(Row(table=self, array=r))

    def values_to_str(self, rows):
        rows_str = []
        for row in rows:
            row_str = []
            for cell in row:
                row_str.append(str(cell))
            rows_str.append(row_str)
        return rows_str

    def column(self, n):
        return [row[n] for row in self.rows_values]

    @property
    def max_columns_widths(self):
        splited = []
        for i in self.rows_values:
            array = []
            for j in i:
                array.append(max(j.split('\n')))
            splited.append(array)
        return [len(max(columns, key=lambda item: len(item))) for columns in zip(*splited)]

    def render(self):
        s = Separator(self)
        out = s.render_up()
        for row in self.rows:
            out += row.render()
        return out + s.render_down()

    @property
    def cell_spacing(self):
        return self.cell_padding + len(self.style.border_y)

    @property
    def cell_padding(self):
        return self.style.padding_left + self.style.padding_right


class Row(object):

    def __init__(self, table, array=[]):
        self.table = table
        self.cell_index = 0
        self.cells_values = array
        self.cells = []
        for item in array: self.add_cell(item)

    def add_cell(self, item):
        self.cells.append(Cell(item, self.cell_index, self.table))
        self.cell_index += 1

    def render(self):
        y = self.table.style.border_y
        out = '%s' % y
        out += ("%s" % y).join( [cell.render() for cell in self.cells] )
        return (out + '%s\n' % y)


class Cell(object):

    def __init__(self, value, index, table):
        self.value = value
        self.index = index
        self.table = table
        self._alignment = 'left'

    @property
    def lines(self):
        return self.value.split('\n')

    def value_for_column_width_recalc(self):
        return max(self.lines)

    @property
    def alignment(self):
        return self._alignment

    @alignment.setter
    def alignment(self, option):
        if option not in ['left', 'center', 'right']:
            raise InvalidOptionError
        self._alignment = option

    def render(self, line=0):
        left = " " * self.table.style.padding_left
        right = " " * self.table.style.padding_right
        out = format(self.lines[line], "%ds" % self.table.max_columns_widths[self.index])
        return "{left}{out}{right}".format(left=left, out=out, right=right)


class Separator(Row):

    def render_up(self):
        return self.render(up=True)

    def render_down(self):
        return self.render(up=False)

    def render(self, up):
        t = self.table
        s = t.style
        n = '\n' if up else ''
        return (
                ('%s%s' % (s.border_i, s.border_x)) +
                ('%s%s%s' % (s.border_x, s.border_i, s.border_x))
                .join( s.border_x * width for width in t.max_columns_widths )
                + '%s%s%s' % (s.border_x, s.border_i, n)
               )


class Style(object):

    def __init__(self, border_x='-', border_y='|', border_i='+',
                padding_right=1, padding_left=1, width=None, alignment=None):
        self.border_x = border_x
        self.border_y = border_y
        self.border_i = border_i
        self.padding_left = padding_left
        self.padding_right = padding_right
        self.width = width
        self.alignment = alignment


class InvalidOptionError(Exception):
    pass

