"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from itertools import chain, cycle
from time import sleep


class TrafficLight:
    __states = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    def __init__(self):
        self.__color = None
        self.__direction = {  # directions of allowed transfers
            from_: to_ for from_, to_ in
            zip(chain((None,), self.__states), cycle(self.__states))
        }

    def running(self, seq=None):
        for color in seq or cycle(self.__states):
            if color == self.__direction[self.__color]:
                self.__color = color
                print(color)
                sleep(self.__states[color])
            else:
                print("Ошибка! Неверный цвет.")
                break


tl = TrafficLight()
tl.running(["красный", "желтый", "зеленый", "синий", "белый"])
