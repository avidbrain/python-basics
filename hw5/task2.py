"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


# Считаем, что слово должно содержать хотя бы одну цифру или букву.
def hasalnum(string):
    """Checks if a string contains at least one alphanumeric symbol."""
    return any(map(lambda x: x.isalnum(), string))


try:
    with open('wiki.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
        lines = content.splitlines()
        print(f"Всего строк: {len(lines)}.")
        for i, line in enumerate(lines, 1):
            words = [word for word in line.split() if hasalnum(word)]
            print(f"Строка {i}, слов: {len(words)}.")
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")
