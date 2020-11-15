from typing import Protocol, List


class Student(Protocol):
    def name(self) -> str: ...
    def courses(self) -> List[str]: ...


class StudentFirstCourse:
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        return f'First course {self._name}'

    def courses(self):
        return ['Math', 'History']


class RejectedStudent:
    def __init__(self, name: str):
        self._name = name

    def name(self) -> None:
        return None


def function(s: Student):
    print('Student name', s.name())
    print('Student courses:', s.courses())


function(StudentFirstCourse('Ivan'))
function(RejectedStudent('Ivan'))