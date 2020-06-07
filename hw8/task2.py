"""
2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivisionPossible(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    user_input = input("Введите делимое и делитель через пробел: ")
    try:
        x, y = map(float, user_input.split())
        break
    except ValueError:
        print("Неверный формат ввода, повторите.")

try:
    if y:
        print(f"Частное равно {x/y}")
    else:
        raise ZeroDivisionPossible('Вообще-то на ноль не делят!')
except ZeroDivisionPossible as e:
    print(e.txt, end=' ')
    print("Но будем считать что частное равно 0.")
