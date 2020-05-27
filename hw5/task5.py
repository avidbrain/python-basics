"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""
import random

# Write
try:
    with open('numbers.txt', 'w', encoding='UTF-8') as wfile:
        for _ in range(100):
            numbers = [f"{random.randint(1, 1001):{5}}" for __ in range(16)]
            print(*numbers, sep='', file=wfile)
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")

# Read and calculate sum
try:
    with open('numbers.txt', 'r', encoding='UTF-8') as rfile:
        content = rfile.read()
        numbers = [int(nm) for nm in content.split() if nm.isdigit()]
        print(sum(numbers))
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")
