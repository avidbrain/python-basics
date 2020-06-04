"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""
# Примечание 1: под "привычным видом" вывода понимаем следующее:
# - визуально отличимые столбцы, выравнивание по правому краю
# - между столбцами один пробел
# Примечание 2: нет проверок и обработки ошибок, чтобы не загромождать
from typing import Iterable, Callable
from operator import add
from itertools import starmap


def ladd(x: Iterable, y: Iterable) -> Iterable:
    """"Vector add two lists"""
    return starmap(add, zip(x, y))


def _ll_str(ll: Iterable[Iterable], to_str: Callable = str) -> str:
    """Convert list of lists to str with each element converted with to_str"""
    return '\n'.join(map(lambda x: ' '.join(map(to_str, x)), ll))


def formatter(colwidth):
    """Decorator to pretty Matrix __str__"""

    def inner(__str__):
        def formatted(*args, **kwargs):
            __str__return = __str__(*args, **kwargs)
            width = max(colwidth, max(map(len, __str__return.split())))
            strings = [row.split() for row in __str__return.splitlines()]
            return _ll_str(strings, lambda x: f"{x:>{width}}")

        return formatted

    return inner


class Matrix:
    def __init__(self, rows):
        self.rows = [row for row in rows]

    def __iter__(self) -> Iterable:
        return iter(self.rows)

    @formatter(10)
    def __str__(self) -> str:
        return _ll_str(self.rows)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        return self.__class__(starmap(ladd, zip(self, other)))


m1 = Matrix([[1, 2, 3, 4], [5, 6, 10 ** 7, 8], [9, 10, 11, 12]])
print("Матрица 1:")
print(m1)
m2 = Matrix([[0, -2, -3, -4], [-5, -5, -10 ** 7, -8], [-9, -10, -10, -12]])
print("Матрица 2:")
print(m2)
print("Сумма матриц:")
print(m1 + m2)
