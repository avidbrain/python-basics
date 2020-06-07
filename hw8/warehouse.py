import sys
from typing import Any, Iterable, Tuple
from collections import deque
import random


class OfficeEquipment:
    _rus = ('Оргтехника', 'оргтехники')
    _all_features = {
        # feature: type-of-choice, list-of-values
        'size': ('single', ('A1', 'A2', 'A3', 'A4')),
        'interface': ('multi', ('USB', 'Wi-Fi', 'Ethernet', 'Bluetooth', 'NFC'))
    }
    _features = {}
    invnum = None  # inventory number

    def __init__(self):
        features = self._all_features.copy()
        features.update(self._features)
        for feature, choice_lov in features.items():
            setattr(self, feature, self.random_feature(choice_lov))

    def __str__(self) -> str:
        features = [getattr(self, feature, '') for feature in ('type', 'size')]
        features = filter(lambda x: x, features)
        return f"{self._rus[0]} {' '.join(features)} №{self.invnum or '-'}"

    @staticmethod
    def random_feature(choice_lov: Tuple[str, Any]) -> Any:
        if choice_lov == 'bool':
            return random.random() > 0.5
        elif choice_lov[0] == 'single':
            return random.choice(choice_lov[1])
        elif choice_lov[0] == 'multi':
            lov = choice_lov[1]
            return random.sample(lov, random.randint(2, len(lov)))
        elif choice_lov[0] == 'range':
            step = choice_lov[1][2]
            return random.randint(*choice_lov[1][:2]) // step * step


class Printer(OfficeEquipment):
    _rus = ('Принтер', 'принтеров')
    _features = {
        'color': 'bool',
        'type': ('single', ('лазерный', 'струйный')),
        'resource': ('range', (10 ** 3, 10 ** 6, 1000))
    }


class Scanner(OfficeEquipment):
    _rus = ('Сканер', 'сканеров')
    _features = {
        'sensor': ('single', ('CCD', 'CIS', 'CMOS'))
    }


class Copier(OfficeEquipment):
    _rus = ('Копир', 'копиров')
    _features = {
        'industrial': ('bool',)
    }


def _get_rus(class_name: str, default: Tuple = ('', '')) -> str:
    """Picks '_rus' property from class given its name"""
    class_ = getattr(sys.modules[__name__], class_name)
    return getattr(class_, '_rus', default)


class NotEnoughStockError(Exception):
    pass


class Warehouse:
    def __init__(self):
        self.__storage = {}
        self.__transfer_log = {}
        self.__last_invnum = 0

    def __str__(self) -> str:
        report = [f"{_get_rus(k)[1]} {v}" for k, v in self.balance.items()]
        report_text = ', '.join(report)
        return f"Склад оргтехники. {report_text.capitalize()}."

    @property
    def balance(self) -> dict:
        """Return stock balance for each type of equipment"""
        return {key: len(value) for key, value in self.__storage.items()}

    def balance_report(self) -> str:
        report = []
        for key, stored in self.__storage.items():
            report.append(f"Список {_get_rus(key)[1]}:")
            report.append('\n'.join(f"\t{str(eq)}" for eq in stored))
        return '\n'.join(report)

    @property
    def log(self) -> dict:
        """Transfer quantity for each department and each type of equipment: """
        return {dept: {key: len(dq) for key, dq in logdict.items()}
                for dept, logdict in self.__transfer_log.items()}

    def log_report(self) -> str:
        report = []
        for department, eq in self.log.items():
            rus = [f"{_get_rus(key)[1]} {value}" for key, value in eq.items()]
            report.append(f"В подразделение '{department}': {', '.join(rus)}.")
        return '\n'.join(report)

    def register(self, batch: Iterable[OfficeEquipment]):
        """Fills in warehouse with equipment"""
        for equipment in batch:
            self.__last_invnum += 1
            equipment.invnum = self.__last_invnum
            key = equipment.__class__.__name__
            if key not in self.__storage:
                self.__storage[key] = deque()
            self.__storage[key].append(equipment)

    def acquire(self, _: str, order: dict):
        """Instantiates equipment from order {equipment_class: quantity}"""
        batch = deque()
        for class_name, num in order.items():
            class_ = getattr(sys.modules[__name__], class_name, None)
            try:
                batch.extend(class_() for _ in range(int(num)))
            except (ValueError, TypeError):
                pass
        self.register(batch)

    def transfer(self, department: str, order: dict):
        """Checks transfer order {equipment_class: quantity} and writes logs"""
        bad_keys = [k for k, n in order.items() if n > self.balance.get(k, 0)]
        if bad_keys:
            report = [_get_rus(key)[1] for key in bad_keys]
            message = f"Недостаточно складских позиций {', '.join(report)}."
            raise NotEnoughStockError(message)
        else:
            if department not in self.__transfer_log:
                self.__transfer_log[department] = {}
            for key, num_ordered in order.items():
                if key not in self.__transfer_log[department]:
                    self.__transfer_log[department][key] = deque()
                for i in range(num_ordered):
                    from_stock = self.__storage[key].popleft()
                    self.__transfer_log[department][key].append(from_stock)
