"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

print("Введите элементы рейтинга, каждый с новой строки.")
print("По окончании ввода введите пустую строку.")
while True:
    user_el = input()
    if user_el:
        if user_el.isdigit():
            user_el = int(user_el)
            if user_el <= my_list[-1]:
                my_list.append(user_el)
            else:
                for i, el in enumerate(my_list):
                    if user_el >= el:
                        my_list.insert(i, user_el)
                        break
            print(my_list)
        else:
            print("Элемент должен быть числом.")
    else:
        break
