"""
Zaimplementuj dekorator klas, który automatycznie uzupełni docstringi wszystkich utworzonych metod w dekorowanej klasie.
Tekst, którym zostaną uzupełnione docstringi będzie przekazywany jako parametr do dekoratora (funkcji tworzącej dekoratory).
Nie zmieniaj docstringów metod specjalnych (takich jak __init__, czy __repr__).
"""
from functools import wraps


def deco_doc(cls):
    method_list = [method for method in dir(cls) if method.startswith('__') is False]
    print(method_list)
    for m in method_list:
        getattr(cls, m).__doc__ = """newdoc"""
    return cls


@deco_doc
class User:
    def __init__(self):
        pass

    def sample(self):
        print('just a test')


if __name__ == '__main__':
    u1 = User()
    u1.sample()
    print(u1.sample().__doc__)
