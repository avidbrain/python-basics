"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом
и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ,
выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def num_input(prompt: str = '', stop: str = 'q') -> tuple:
    """Receives list of numbers from user, checks if `stop` was entered.

    Input strings other than `stop` are ignored.

    Args:
        prompt: message to print to invite user to enter a sequence
        stop: string indicating that user has requested end of input

    Returns:
        tuple: (bool: whether `stop` was entered, list: numbers)
    """
    numbers = []
    has_stop = False
    for user_num in input(prompt).split():
        if user_num == stop:
            has_stop = True
            break
        else:
            try:
                numbers.append(float(user_num))
            except ValueError:
                continue
    return has_stop, numbers


total = 0
enough = False
while not enough:
    enough, numbers = num_input('Введите строчку чисел: ')
    total += sum(numbers)
    print(f"Сумма: {total}")
