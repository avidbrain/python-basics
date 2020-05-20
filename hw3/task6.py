"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
 и возвращающую его же, но с прописной первой буквой.
 Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться
с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word: str) -> str:
    """Capitalizes word of ascii symbols.

    Args:
        word: word to capitalize

    Returns:
        str: capitalized word

    Example:
        >>> int_func('text')
        'Text'
    """
    if word:
        code = ord(word[:1])
        return chr(code - 32 if 97 <= code <= 122 else code) + word[1:]
    else:
        return word


print(*map(int_func, input("Enter text: ").split()))
