"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
from typing import Tuple
import datetime


class Date:
    def __init__(self, datestring: str):
        """ String 'day-month-year' to (day, month, year)."""
        self.datestring = datestring

    @classmethod
    def get_datetuple(cls, datestring: str) -> Tuple[int]:
        return tuple(map(int, datestring.split('-')))

    @staticmethod
    def is_valid(datetuple: Tuple[int]) -> bool:
        try:
            _ = datetime.date(*datetuple[::-1])
            return True
        except (TypeError, ValueError):
            return False


dt = Date.get_datetuple('31-12-1999')
print(dt)
assert Date.is_valid(dt)
dt = Date.get_datetuple('29-02-3000')
print(dt)
assert not Date.is_valid(dt)
