"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(x: float, y: float, z: float) -> float:
    """Calculates sum of 2 largest arguments."""
    a, b = (x, y) if x > y else (y, x)
    return a + z if z > b else x + y
