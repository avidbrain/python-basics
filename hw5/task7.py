"""
7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
from statistics import mean

firms = {}
try:
    with open("firms.txt", "r", encoding="UTF-8") as rfile:
        for line in rfile:
            try:
                *nameparts, ownership, revenue, cost = line.split()
                firms[' '.join(nameparts)] = int(revenue) - int(cost)
            except ValueError:
                continue
    average = {"average_profit": mean(filter(lambda x: x > 0, firms.values()))}

    with open("firms.json", 'w', encoding='UTF-8') as wfile:
        json.dump([firms, average], wfile, ensure_ascii=False)
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")
