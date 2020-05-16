"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_list = []
print("Введите список, каждый элемент с новой строки.")
print("По окончании ввода введите пустую строку.")
while True:
    user_el = input()
    if user_el:
        user_list.append(user_el)
    else:
        if user_list:
            break
        else:
            print("Вы ввели пустой список, попробуйте ещё раз.")

user_list_backup = user_list.copy()

print('#' * 20)
print("Вариант с операциями в самом списке")
i = 0
while i + 1 < len(user_list):
    el = user_list.pop(i + 1)
    user_list.insert(i, el)
    i += 2
print(user_list)

user_list = user_list_backup

print('#' * 20)
print("Вариант с созданием нового списка")
result = []
i = 0
while i < len(user_list):
    pair = user_list[i:i + 2]
    result.extend(pair[::-1])
    i += 2
print(result)
