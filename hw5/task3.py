"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
from string import whitespace, punctuation
from statistics import mean

salary_info = {}
try:
    with open('salary.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            # Format: surname <not used> salary(integer) <not used>
            name = None
            salary = None
            for word in line.split():
                if word.isdigit():
                    salary = int(word)
                    break
                elif not name:
                    name = word
            if name is not None and salary is not None:
                salary_info[name.strip(whitespace + punctuation)] = salary
    below20 = [name for name, salary in salary_info.items() if salary < 20000]
    print("Сотрудники с окладом менее 20 тыс:", ', '.join(below20))
    print("Средний оклад:", mean(salary_info.values()))
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")
