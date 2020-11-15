from typing import Callable, Tuple

MyFunc = Callable[[int], Tuple[int, str]]


def f1(value: int) -> int:
    return value


def consumer(f: MyFunc):
    pass

consumer(f1)


MyFunc1 = Callable[..., int]


def consumer1(f: MyFunc1):
    pass

consumer1(f1)
