"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str,
                 wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def get_total_income(self) -> int:
        return self._income['wage'] + self._income['bonus']


director = Position('Пётр', 'Петров', 'Директор', 100000, 30000)
manager = Position('Семён', 'Продажник', 'Менеджер', 70000, 30000)

assert director.name == 'Пётр'
assert director.surname == 'Петров'
assert director.position == 'Директор'
assert director.get_full_name() == 'Петров Пётр'
assert director.get_total_income() == 130000

assert manager.name == 'Семён'
assert manager.surname == 'Продажник'
assert manager.position == 'Менеджер'
assert manager.get_full_name() == 'Продажник Семён'
assert manager.get_total_income() == 100000
