"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class AbstractGarment(ABC):
    @abstractmethod
    def fabric(self):
        pass


class Garment(AbstractGarment):
    def __init__(self, name):
        self.name = name

    @property
    def fabric(self) -> float:
        return 0

    def __add__(self, other: 'Garment') -> float:
        return self.fabric + other.fabric


class Coat(Garment):
    def __init__(self, name: str, V: int):
        super().__init__(name)
        self.V = V

    @property
    def fabric(self) -> float:
        return self.V/6.5 + 0.5


class Suit(Garment):
    def __init__(self, name, H: int):
        super().__init__(name)
        self.H = H

    @property
    def fabric(self) -> float:
        return 2 * self.H + 0.3


my_coat = Coat('Моё пальто', 54)
my_suit = Suit('Мой костюм', 5)
print(f"Общий расход ткани: {my_coat + my_suit:.2f} метров.")
