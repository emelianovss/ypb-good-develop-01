class MyClass:
    def __init__(self, s):
        self.s = s


def function(c: MyClass) -> str:
    return c.copy().upper()


function(MyClass('string'))
