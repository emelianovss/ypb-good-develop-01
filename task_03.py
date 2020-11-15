def my_function(val_1, val_2):
    if isinstance(val_1, int):
        return [bool(v % val_1) for v in val_2]
    elif isinstance(val_1, str):
        return [val_1 in v for v in val_2]
    else:
        raise TypeError('val_1 must be string or int')


my_function(10, [100, 200, 35, 40, 20])
my_function('c', ['hello', 'clock', 'why', 'course', 'try'])
