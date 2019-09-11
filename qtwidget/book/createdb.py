from PySide2.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from datetime import datetime


def add_book(q: QSqlQuery, title: str, year: int, author_id: int, genere_id: int, rating: int) -> None:
    q.addBindValue(title)
    q.addBindValue(year)
    q.addBindValue(author_id)
    q.addBindValue(genere_id)
    q.addBindValue(rating)
    q.exec_()


def add_genre(q: QSqlQuery, name: str) -> int:
    q.addBindValue(name)
    q.exec_()
    return q.lastInsertId()


def add_author(q: QSqlQuery, name: str, birthdate: datetime) -> int:
    q.addBindValue(name)
    q.addBindValue(birthdate)
    q.exec_()
    return q.lastInsertId()
