from typing import Union, Type

Number = Union[float, int]


def func(value: str, type_: Type[Number]) -> Number:
    return type_(value)
