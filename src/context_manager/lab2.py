# lab2
# Zadanie polega wykorzystaniu context managera jako timera. Tak uzupełnij poniższa klasę aby przeszedł test
# /tests/context_manager/test_lab2.py
import time


class Timer:
    def __init__(self):
        self._start = None
        self.time = 0

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.time += int(self.end - self._start)
        self._start = None


def run_timer():
    with Timer() as timer:
        time.sleep(1)
    return timer.time


if __name__ == '__main__':
    print(run_timer())
