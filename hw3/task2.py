"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

USER_VARS = {
    'first_name': 'Имя',
    'last_name': 'Фамилия',
    'year_of_birth': 'Год рождения',
    'city': 'Город проживания',
    'email': 'email',
    'phone': 'Телефон'
}


def user_info(first_name: str,
              last_name: str,
              year_of_birth: int,
              city: str,
              email: str,
              phone: str,
              sep: str = '; ') -> str:
    """Builds user description str, 'key: value' pairs, separated by `sep`."""
    kwargs = locals()
    del kwargs['sep']
    result = []
    for key, value in kwargs.items():
        result.append(f"{USER_VARS.get(key, key)}: {value}")
    return sep.join(result)
