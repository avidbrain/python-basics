"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def get_numbers(string):
    """Picks numbers from a string"""
    filtered = filter(lambda x: x.isdigit() or x.isspace(), string)
    return [int(n) for n in ''.join(filtered).split()]


curriculum = {}

try:
    with open('curriculum.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            try:
                subject, numinfo = line.split(':')
                curriculum[subject.strip()] = sum(get_numbers(numinfo))
            except ValueError:
                continue
    print(curriculum)
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")
