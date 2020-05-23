"""
5. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
import sys
from itertools import cycle, islice

if __name__ == "__main__":
    base = ("тройка", "семёрка", "туз")
    try:
        times = int(sys.argv[1])
        if times > 0:
            seq = islice(cycle(base), times)
            print(", ".join(seq))
    except (IndexError, ValueError):
        print(f"{sys.argv[0]} <количество элементов всего>")
