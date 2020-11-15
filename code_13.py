from typing import TypeVar, List, Dict


def function1(value: int, string: str, other: List[bool]) -> int:
    return other


T = TypeVar('T')


def function2(items: List[T]) -> Dict[str, T]:
    return {str(i): items[i] for i in range(len(items))}


function2(['a', 'b', 'c'])[0]