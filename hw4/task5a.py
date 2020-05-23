"""
5. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
import sys
from itertools import count, islice

if __name__ == "__main__":
    try:
        start, last = [int(arg) for arg in sys.argv[1:]]
        if last >= start:
            seq = islice(count(start), last - start + 1)
            print(",".join(map(str, seq)))
    except ValueError:
        print(f"{sys.argv[0]} первый последний")
