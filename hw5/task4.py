"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
vocab = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять'
}
try:
    with open('engnum.txt', 'r', encoding='UTF-8') as rfile, \
            open('rusnum.txt', 'w', encoding='UTF-8') as wfile:
        for line in rfile:
            translated = [vocab.get(word, word) for word in line.split()]
            print(*translated, file=wfile)
except IOError as ioe:
    print(f"Ошибка '{ioe.strerror}' при работе с файлом '{ioe.filename}'.")
