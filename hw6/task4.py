"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random


class Car:
    def __init__(self, speed: float, color: str, name: str,
                 is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        print(f"Машина повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Внимание, превышение скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Внимание, превышение скорости!")


class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_police = True


town = TownCar(50, 'Синий', 'Городской')
sport = SportCar(100, 'Красный', 'Спортивный')
work = WorkCar(50, 'Белый', 'Рабочий')
police = PoliceCar(50, 'Черный', 'С мигалкой')
undercover = SportCar(80, 'Серый', 'Незаметный', True)

for car in (town, sport, work, police, undercover):
    print(20 * '*')
    print(f"{car.color} {car.name.lower()} автомобиль.")
    if car.is_police:
        print("Это полицейская машина.")
    car.go()
    car.show_speed()
    car.turn(random.choice(('направо', 'налево')))
    car.turn(random.choice(('направо', 'налево')))
    car.stop()
