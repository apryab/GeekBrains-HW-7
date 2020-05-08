from abc import ABC, abstractmethod


def my_decorator(func):

    def wrapper(self):
        if hasattr(self, 'size'):
            print('Количество ткани для пальто -', end=' ')
        if hasattr(self, 'height'):
            print('Количество ткани для костюма -', end=' ')
        answer = func(self)
        print(answer)
    return wrapper


class Clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric_count(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        super().__init__()
        try:
            self.size = int(size)
        except(TypeError, ValueError):
            print('Неправильный формат роста. Будет присвоено значение -1')
            self.size = -1

    @my_decorator
    def fabric_count(self):
        if self.size <= 0:
            raise ValueError
        else:
            return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, height):
        super().__init__()
        try:
            self.height = float(height)
        except(TypeError, ValueError):
            print('Неправильный формат роста, надо ввести число.')
            self.height = -1

    @my_decorator
    def fabric_count(self):
        if self.height <= 0:
            raise ValueError
        else:
            return 2 * self.height + 0.3


my_coat_1 = Coat(5)
my_costume = Costume(4)
my_coat_2 = Coat('r')
try:
    my_coat_1.fabric_count()
    my_costume.fabric_count()
    my_coat_2.fabric_count()
except(TypeError, ValueError):
    print('\n')
    print('Неправильный формат данных у объекта')
