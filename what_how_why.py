class MyClass:
    def __init__(self, name: str):
        self._name = name

    def change_name(self, new_name: str):
        self._name = new_name

    def get_name(self) -> str:
        return self._name


def func(item: MyClass):
    print(item.get_name().lower())


my_obj = MyClass('name')
my_obj.set_name(10)

if __name__ == '__main__':
    func(my_obj)