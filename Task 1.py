import copy


class Matrix:

    def __init__(self, my_list):
        mistake = 0
        try:
            len(my_list)
        except TypeError:
            print('Матрица должна быть списком списков')
            mistake = 1
        if mistake != 1:
            if len(my_list) > 0:
                try:
                    n = len(my_list[0])
                except TypeError:
                    print('Матрица должна быть списком списков')
                    n = -1
                    mistake = 1
                try:
                    if mistake != 1:
                        for elem in my_list:
                            if len(elem) != n:
                                mistake = 1
                                break
                            for item in elem:
                                float(item)
                except(ValueError, TypeError):
                    print('Неправильный формат данных в матрице')
                    mistake = 1
                if mistake == 0:
                    self.height = len(my_list)
                    self.width = len(my_list[0])
                    self.list = my_list
            else:
                mistake = 1
            if mistake == 1:
                self.height = 0
                self.width = 0
                self.list = []
                print('Будет создана матрица нулевого размера')

    def __str__(self):
        big_str = '['
        for elem in self.list:
            big_str += '['
            for item in elem:
                big_str += str(item)
                big_str += ', '
            if self.width > 0:
                big_str = big_str[:-2]
            big_str += ']'
            big_str += ', '
        if self.height > 0:
            big_str = big_str[:-2]
        big_str += ']'
        return big_str

    def __add__(self, other):
        if type(other) == Matrix:
            if(self.width == other.width) and (self.height == other.height):
                answer_list = []
                for i in range(len(self.list)):
                    temp_list = []
                    for j in range(len(self.list[i])):
                        temp_list.append(self.list[i][j] + other.list[i][j])
                    answer_list.append(copy.deepcopy(temp_list))
                    temp_list.clear()
                return Matrix(answer_list)
            else:
                print('Размеры матриц не равны')
                return ValueError
        else:
            print('Неправильные типы данных операндов')
            return TypeError


my_matrix_1 = Matrix([[1, 100, 6], [2, 5, 1], [5, 8, 1]])
my_matrix_2 = Matrix([[2, 5, 8], [1, 4, 2], [2, 7, 3]])
answer_matrix = my_matrix_1 + my_matrix_2
print(answer_matrix)
