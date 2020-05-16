"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

product_db = []
record_keys = "название", "цена", "количество", "eд"
i = 0
print("Введите информацию о товарах.")
print("Для окончания ввода вместо названия введите пустую строку.")
while True:
    i += 1
    print("Товар", i)
    product_name = input("Введите название: ")
    if product_name:
        while True:
            product_price = input("Введите цену (целое число): ")
            if product_price.isdigit():
                product_price = int(product_price)
                break
            else:
                print("Неверный ввод, повторите.")
        while True:
            product_quant = input("Введите количество (целое число): ")
            if product_quant.isdigit():
                product_quant = int(product_quant)
                break
            else:
                print("Неверный ввод, повторите.")
        product_unit = input("Введите единицу измерения: ")
        product_tpl = product_name, product_price, product_quant, product_unit
        record = dict(zip(record_keys, product_tpl))
        product_db.append((i, record))
    else:
        break
# Analytics
analyt = {}
for key in record_keys:
    analyt[key] = set()
for _, record in product_db:
    for key in record_keys:
        analyt[key].add(record[key])
# Result is dict of lists not sets
result = {}
for key in record_keys:
    result[key] = list(analyt[key])
print(result)
