"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия
одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    weight_sqm = 25

    def __init__(self, length: int, width: int):
        """Length and width of the road in meters."""
        self._length = length
        self._width = width

    def asphalt(self, thickness: int = 5) -> float:
        """Calculates asphalt weight in tons given required thickness in cm."""
        return self._length * self._width * self.weight_sqm * thickness / 1000


road = Road(5000, 20)
print(road.asphalt(5))
