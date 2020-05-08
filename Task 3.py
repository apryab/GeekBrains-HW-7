class Cell:

    def __init__(self, numb_of_cells):
        try:
            self.numb_of_cells = float(numb_of_cells)
            if self.numb_of_cells % 1 == 0:
                self.numb_of_cells = int(self.numb_of_cells)
                if self.numb_of_cells == 0:
                    print('В ячейке не может быть 0 клеток. Будет создана единичная клетка')
                    self.numb_of_cells = 1
            else:
                print('Неправильный формат данных. Будет создана единичная клетка')
                self.numb_of_cells = 1
        except(ValueError, TypeError):
            print('Ошибка в формате данных. Будет создана единичная клетка')
            self.numb_of_cells = 1

    def __add__(self, other):
        if type(other) == Cell:
            sum_of_two = self.numb_of_cells + other.numb_of_cells
            return Cell(sum_of_two)
        else:
            print('Неправильный тип операндов. Будет создана единичная клетка')
            return Cell(1)

    def __mul__(self, other):
        if type(other) == Cell:
            multi_of_two = self.numb_of_cells * other.numb_of_cells
            return Cell(multi_of_two)
        else:
            print('Неправильный тип операндов. Будет создана единичная клетка')
            return Cell(1)

    def __sub__(self, other):
        if type(other) == Cell:
            sub_of_two = self.numb_of_cells - other.numb_of_cells
            if sub_of_two <= 0:
                print('Клеток в ячейке не может быть меньше нуля. Будет создана единичная клетка')
                return Cell(1)
            else:
                return Cell(sub_of_two)
        else:
            print('Неправильный тип операндов. Будет создана единичная клетка')
            return Cell(1)

    def __truediv__(self, other):
        if type(other) == Cell:
            div_of_two = self.numb_of_cells // other.numb_of_cells
            if div_of_two != 0:
                return Cell(div_of_two)
            else:
                print('Количество ячеек в первой клетке должно быть больше чем во второй.', end=' ')
                print('Будет создана единичная клетка')
                return Cell(1)
        else:
            return Cell(1)

    def make_order(self, numb_in_row):
        try:
            row_numb = float(numb_in_row)
            answer_str = ''
            if row_numb != 0:
                if row_numb % 1 == 0:
                    row_numb = int(row_numb)
                    for i in range(1, self.numb_of_cells + 1):
                        answer_str += '*'
                        if i % row_numb == 0:
                            if i != self.numb_of_cells:
                                answer_str += '\n'
                    return answer_str
                else:
                    print('Неправильный формат данных. Будет создана пустая строка')
                    return ''
            else:
                print('Ячеек в ряду не может быть ноль. Будет создана пустая строка')
                return ''

        except(TypeError, ValueError):
            print('Введите целое число в качестве длины строки. Будет создана пустая строка')
            return ''


my_cell_1 = Cell(8)
my_cell_2 = Cell(5)
my_cell_3 = Cell(5.3)
print((my_cell_1 + my_cell_2).numb_of_cells)
print((my_cell_1 - my_cell_2).numb_of_cells)
print((my_cell_1 * my_cell_2).numb_of_cells)
print((my_cell_1 / my_cell_2).numb_of_cells)
print(my_cell_1.make_order(0))
