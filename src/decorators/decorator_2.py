"""
Zaimplementuj dekorator klas, który automatycznie uzupełni docstringi wszystkich utworzonych metod w dekorowanej klasie.
Tekst, którym zostaną uzupełnione docstringi będzie przekazywany jako parametr do dekoratora (funkcji tworzącej dekoratory).
Nie zmieniaj docstringów metod specjalnych (takich jak __init__, czy __repr__).
"""


def deco_doc(new_docstring):
    def decorator(cls):
        method_list = [method for method in dir(cls) if method.startswith('__') is False]
        # print(method_list)
        for m in method_list:
            getattr(cls, m).__doc__ = new_docstring
        return cls
    return decorator


@deco_doc('docstring updated by deco_doc')
class User:
    def __init__(self, name):
        self.name = name

    def sample(self):
        """
        printing sample message
        :return:
        """
        print(f'just a test for {self.name}')

    def hello(self):
        """
        says hello to you
        :return:
        """
        print(f'Hello, {self.name}')


if __name__ == '__main__':
    u1 = User('Bartosz')
    print(f'function: {u1.__init__.__name__}, docstring: {u1.__init__.__doc__}')
    print(f'function: {u1.sample.__name__}, docstring: {u1.sample.__doc__}')
    print(f'function: {u1.hello.__name__}, docstring: {u1.hello.__doc__}')
