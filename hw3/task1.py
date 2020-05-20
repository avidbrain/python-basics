"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def get_numeric(prompt: str = ": ", invalid: str = "") -> float:
    """Receives float from user.
     On error, prints `invalid_msg` and retries input indefinitely.

    Args:
        prompt: message to print to invite user to enter a number
        invalid: message to print to inform user of an input error

    Returns:
        float: numeric input from user
    """

    while True:
        try:
            result = float(input(prompt))
            break
        except ValueError:
            print(invalid)
    return result


MSG_PROMPT = "Введите число: "
MSG_INVALID = "Неверный ввод, повторите."


def input_divide() -> float:
    """Returns quotient of two numbers (user input) or 0 on zero divider."""
    try:
        return (
                get_numeric(MSG_PROMPT, MSG_INVALID) /
                get_numeric(MSG_PROMPT, MSG_INVALID)
        )
    except ZeroDivisionError:
        return 0
