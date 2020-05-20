"""
4. Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа
в степень.
"""


def my_func(x: float, y: int) -> float:
    """Calculates x to the power of y.

    Args:
        x: positive float
        y: negative integer

    Returns:
        float: x to the power of y
    """
    if x in (0, 1):
        return x
    else:
        result = 1
        counter = 1
        while counter <= abs(y):
            result /= x
            counter += 1
        return result
