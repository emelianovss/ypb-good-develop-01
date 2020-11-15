from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from code_03 import ImportClass


def function(c: 'ImportClass'):
    print('This is function call')


if __name__ == '__main__':
    print('Main call')
