# lab1
# Uzupełnij klase tak aby test wykorzystujący ją przeszedł poprawnie
# /tests/context_manager/test_lab1.py
# Zaimplementuj context manager za pomocą klasy

class MyContextManager:
    def __init__(self):
        pass
        # print('__init__')

    def __enter__(self):
        # print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # print('__exit__')


if __name__ == '__main__':
    print('test')