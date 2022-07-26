# lab4
# Napisz manager contextu wspierający operacje na bazie danych w naszym przypadku sqllite
# https://docs.python.org/3/library/sqlite3.html
# /tests/context_manager/test_lab4.py
import sqlite3
from contextlib import contextmanager


@contextmanager
def open_db(file_name: str):
    connection = sqlite3.connect(file_name)
    cur = connection.cursor()
    yield cur
    connection.commit()
    connection.close()
