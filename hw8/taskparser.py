from typing import Any, Optional, Union, Iterator, List
import shlex


class MarkedToken:
    @staticmethod
    def mark_token(token: str) -> Any:
        return None

    def __init__(self, token: str, value: Any = None):
        self.token = token
        if value is None:
            self.value = self.mark_token(token)
        else:
            self.value = value

    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}({str(self.value)})" if self.value else self.token


class Num(MarkedToken):
    """Numeric token"""

    @staticmethod
    def mark_token(token: str) -> Union[None, float]:
        try:
            return float(token)
        except ValueError:
            return None


class End(MarkedToken):
    """End of sentence token"""
    markers = '.!?'

    @staticmethod
    def mark_token(token: str) -> Union[None, str]:
        return token if token and token[-1] in End.markers else None


class StartsWith(MarkedToken):
    """Parent class for dictionary-based marking"""
    markers = {}

    @classmethod
    def mark_token(cls, token: str) -> Union[None, str]:
        tkn = token.lower()
        result = None
        for key, value in cls.markers.items():
            if tkn.startswith(key):
                result = value
                break
        return result


class Cmd(StartsWith):
    """Command part of a task string"""
    markers = {'принять': 'acquire', 'передать': 'transfer'}


class Product(StartsWith):
    """Product of a task string"""
    markers = {'принтер': 'Printer', 'сканер': 'Scanner', 'копир': 'Copier'}


class TokenMarker:
    """Tries all available markers on a token, in a specific order"""

    def __new__(cls, *args, **kwargs):
        cls.__order = (Num, End, Cmd, Product)
        return super().__new__(cls)

    def __call__(self, token: str) -> Union[str, MarkedToken]:
        """Marks one token"""
        marked = token
        for class_ in self.__order:
            value = class_.mark_token(token)
            if value is not None:
                marked = class_(token, value)
                break
        return marked


def parse_sentence(sentence: List) -> Union[None, dict]:
    """Builds task implementation tree for one task"""
    head = sentence[0]
    tail = sentence[-1]
    if isinstance(head, Cmd) and isinstance(tail, str):
        action = head.value
        direction = tail
        order = {}
        for i, token in enumerate(sentence[1:-1]):
            if isinstance(token, Product):
                pre_token = sentence[i]
                quantity = pre_token.value if isinstance(pre_token, Num) else 1
                order[token.value] = int(order.get(token.value, 0) + quantity)
        task = {action: (direction, order)}
    else:
        task = None
    return task


def sentences(seq: Iterator[Union[str, MarkedToken]]):
    """Picks sentences from sequence of tokens"""
    sentence = []
    for marked in seq:
        if isinstance(marked, End):
            yield sentence
            sentence = []
        else:
            sentence.append(marked)
    if sentence:
        yield sentence


def parse(programme: str) -> List[Optional[dict]]:
    """Converts text programme (action plan) into sequence of tasks"""
    tokens = shlex.shlex(programme, posix=True, punctuation_chars=",;.!?")
    tokens.whitespace_split = True
    tm = TokenMarker()
    tasklist = []
    for sentence in sentences(map(tm, tokens)):
        task = parse_sentence(sentence)
        if task:
            tasklist.append(task)
    return tasklist
