"""
4. «Склад оргтехники». Класс, описывающий склад. Класс «Оргтехника».
Классы-наследники — конкретные типы оргтехники (принтер, сканер, ксерокс).
5. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании.
6. Механизм валидации вводимых пользователем данных.
"""
from warehouse import Warehouse, NotEnoughStockError
import taskparser

programme = """
Принять 3 принтера, 3 сканера и 3 копира на склад.
Передать принтер и копир подразделению 'Отдел кадров'.
Передать 2 сканера отделу 'Маркетинг'.
Передать копир, сканер и 2 принтера отделу 'Развитие бизнеса'.
Передать принтер и сканер отделу 'ИТ'. # Будет ошибка
Принять 3 принтера и сканер на склад.
Передать 2 принтера и сканер отделу 'ИТ'.
"""

wh = Warehouse()
for task in taskparser.parse(programme):
    for method_name, (department, order) in task.items():
        method = getattr(wh, method_name)
        try:
            method(department, order)
        except NotEnoughStockError as e:
            print(e)
        except (TypeError, ValueError):
            pass

print(wh)
print('=' * 7, "Итог выдачи со склада", '=' * 7)
print(wh.log_report())
print('=' * 7, "Отчет по остаткам", '=' * 7)
print(wh.balance_report())
