"""
Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
powinna natomiast zwrócić string, z komunikatem:
"add typings to function <nazwa_funkcji>, please!"
gdzie nazwa_funkcji jest nazwą dekorowanej funkcji.
"""
from functools import wraps


def require_typing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not func.__annotations__:
            return f'add typings to function {func.__name__}, please!'
        else:
            if 'return' not in func.__annotations__ or len(func.__annotations__) == 1:
                return f'Add typing to function {func.__name__}, please!'
            else:
                return func(*args, **kwargs)
    return wrapper


@require_typing
def add_with_typings(a: float, b: float) -> float:
    return a + b


@require_typing
def add_with_vars(a: float, b: float):
    return a + b


@require_typing
def add_with_result(a, b) -> float:
    return a + b


@require_typing
def add_without_typings(a, b):
    return a + b


if __name__ == '__main__':
    print(add_with_typings(1.2, 2.3))
    print(add_with_vars(1.2, 2.3))
    print(add_with_result(1.2, 2.3))
    print(add_without_typings(1.2, 2.3))
