from typing import TypeVar, List

T = TypeVar('T', int, List[int])


def func(value: T):
    pass

func(10)
func([10])
func('10')