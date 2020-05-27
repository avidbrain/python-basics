"""
1. Создать программно файл в текстовом формате, записать в него построчно данные
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
try:
    with open('user_input.txt', 'w', encoding='UTF-8') as wfile:
        while True:
            line = input()
            if line:
                print(line, file=wfile)
            else:
                break
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")
