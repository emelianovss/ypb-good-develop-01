from typing import TypeVar

class Parent:
    pass

class Child(Parent):
    pass

class Some:
    pass


T = TypeVar('T', bound=Parent)


def func(value: T):
    pass

func(Parent())
func(Child())
func(Some())