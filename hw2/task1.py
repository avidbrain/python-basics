"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

type_check = {
    "Тип NoneType": (type(None),),
    "Числовое значение": (int, float, complex),
    "Строка": (str,),
    "Логическое значение": (bool,),
    "Коллекция": (list, dict, set),
    "Двоичные данные": (bytes, bytearray)
}

user_list = [None, 0, 0.1, complex(-1, -1), "Привет", False,
             [1, 2], {3, 4}, {5: 6},
             bytes([10, 20, 30, 40]), bytearray([10, 20, 30, 40]),
             zip([0, 1], [10, 11])]

for el in user_list:
    prefix = ""
    for key, type_tpl in type_check.items():
        if type(el) in type_tpl:
            prefix = key
            break
    if not prefix:
        prefix = str(type(el))
    print(prefix, el, sep=": ")
