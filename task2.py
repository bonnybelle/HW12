# 2. Реализовать класс singleton (использовать декоратор)

import functools


def singleton(cls):
    instances = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class MyClass:
    ...


print(id(MyClass()))
print(id(MyClass()))
