# Задача 1. Переменные
some_text = "Несколько строк текста:\n\tпервая,\n\tвторая,\n\tтретья."
print(some_text)

math_result = 2020 / 5
print("Число 2020 делится на 5 без остатка, но выдаёт float:", math_result)

input_string = input("Введите строку: ")
print('Вы ввели "{}".'.format(input_string))

while True:
    input_number = input("Введите целое число: ")
    if input_number.isnumeric():
        print("Вы ввели число {}.".format(input_number))
        break
    else:
        print("Ввод неверный, повторите.")

# Задача 2. ЧЧ:ММ:СС
input_time_sec = input("Введите время в секундах: ")
if input_time_sec.isdigit():
    time_sec = int(input_time_sec)
    time_hh = time_sec // 3600
    time_mm = (time_sec % 3600) // 60
    time_ss = time_sec % 60
    print("{:02d}:{:02d}:{:02d}".format(time_hh, time_mm, time_ss))
else:
    print("Ввод неверный!")

# Задача 3. n + nn + nnn
input_n = input("Введите n: ")
if input_n.isnumeric():
    n = int(input_n)
    nn = int(input_n + input_n)
    nnn = int(input_n + input_n + input_n)
    print(n + nn + nnn)
else:
    print("Ввод неверный!")

# Задача 4. Наибольшая цифра
input_n = input("Введите целое положительное число: ")
if input_n.isnumeric():
    n = int(input_n)
    max_digit = n % 10
    digits_left = n // 10
    while digits_left:
        last_digit = digits_left % 10
        if last_digit > max_digit:
            max_digit = last_digit
        digits_left = digits_left // 10
    print(max_digit)
else:
    print("Ввод неверный!")

# Задача 5. Фирма
input_revenue = input("Введите значение выручки: ")
input_cost = input("Введите значение издержек: ")
if input_revenue.isnumeric() and input_cost.isdigit():
    revenue = int(input_revenue)
    cost = int(input_cost)
    if revenue > cost:
        print("Фирма работает с прибылью.")
        profit = revenue - cost
        profitability = (revenue - cost) / revenue
        print("Рентабельность выручки: {:.2%}".format(profitability))
        input_personnel = input("Введите численность сотрудников: ")
        if input_personnel.isdigit():
            personnel = int(input_personnel)
            print("Прибыль на одного сотрудника: {}".format(profit / personnel))
        else:
            print("Ввод неверный!")
    elif revenue < cost:
        print("Фирма работает с убытком.")
    else:
        print("Фирма работает с нулевой рентабельностью.")
else:
    print("Ввод неверный!")

# Задача 6. Спортсмен
input_a = input("Введите a, результат первого дня: ")
input_b = input("Введите b, целевой результат: ")
if input_a.isdigit() and input_b.isdigit():
    a = int(input_a)
    b = int(input_b)
    n = 1
    result = a
    while result < b:
        n = n + 1
        result = result * 1.1
    print(n)
else:
    print("Ввод неверный!")
