from typing import Union

MyNum = Union[str, int]


def func(n: MyNum):
    return n


func(10)

func('10')

func(10.0)
