"""
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству клеток (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток,
соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки
должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять
только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, num: int):
        self.num = num

    def __str__(self):
        return f"Клетка-{self.num}"

    def __raise_on_bad_type(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Операция работает только между Клетками.")

    def __add__(self, other):
        self.__raise_on_bad_type(other)
        return Cell(self.num + other.num)

    def __gt__(self, other):
        self.__raise_on_bad_type(other)
        return self.num > other.num

    def __sub__(self, other):
        self.__raise_on_bad_type(other)
        if self > other:
            return Cell(self.num - other.num)
        else:
            print("Вычитание недопустимо.")
            return None

    def __mul__(self, other):
        self.__raise_on_bad_type(other)
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        self.__raise_on_bad_type(other)
        return Cell(self.num // other.num)

    def make_order(self, ncol):
        # Короткий код после обсуждения родился такой:
        # return '\n'.join('*' * min(self.num - i, ncol)
        #                  for i in range(0, self.num, ncol))
        # Ниже длинный код, который был написан вначале
        full_rows = self.num // ncol
        leftover = self.num % ncol
        result = ""
        if full_rows:
            result = '\n'.join('*' * ncol for _ in range(full_rows))
        if leftover:
            result += '\n' + '*' * leftover
        return result


c1 = Cell(11)
c2 = Cell(3)
print(c1+c2)
print(c1-c2)
print(c2-c1)
print(c1*c2)
print(c1/c2)
print(c1.make_order(6))
