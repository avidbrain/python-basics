"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons = ["зима", "весна", "лето", "осень"]

while True:
    user_num = input('Введите номер месяца, 1 - 12: ')
    if user_num.isdigit():
        month_num = int(user_num)
        if 1 <= month_num <= 12:
            break
    print('Ошибка ввода, повторите.')

print('#' * 20)
print("Вариант со списком")
print(seasons[(month_num % 12) // 3])

print('#' * 20)
print("Вариант со словарем")
season_dict = {}
season_num = 12
for season in seasons:
    for _ in range(3):
        season_dict[((season_num - 1) % 12) + 1] = season
        season_num += 1
print(season_dict[month_num])
