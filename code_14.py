from typing import List, ClassVar


class MyClass:
    value_1: int
    value_2: List[str]
    value_3: ClassVar[bool] = 10

    def __init__(self, value_1: str, value_2: int):
        self.value_1 = value_1
        self.value_2 = value_2

    def method(self, value: List[bool]):
        self.value_1 = value
