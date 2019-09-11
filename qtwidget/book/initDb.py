from PySide2.QtSql import QSqlDatabase, QSqlQuery
from createdb import *

BOOKS_SQL = """
    create table books(id integer primary key, title varchar, author integer,
                       genre integer, year integer, rating integer)
    """
AUTHORS_SQL = """
    create table authors(id integer primary key, name varchar, birthdate date)
    """
GENRES_SQL = """
    create table genres(id integer primary key, name varchar)
    """
INSERT_AUTHOR_SQL = """
    insert into authors(name, birthdate) values(?, ?)
    """
INSERT_GENRE_SQL = """
    insert into genres(name) values(?)
    """
INSERT_BOOK_SQL = """
    insert into books(title, year, author, genre, rating)
                values(?, ?, ?, ?, ?)
    """


def init_db() -> None:
    def check(func, *args):
        if not func(*args):
            raise ValueError(func.__self__.lastError())

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(":memory:")

    check(db.open)

    q = QSqlQuery()
    check(q.exec_, BOOKS_SQL)
    check(q.exec_, AUTHORS_SQL)
    check(q.exec_, GENRES_SQL)
    check(q.prepare, INSERT_AUTHOR_SQL)

    asimovId = add_author(q, "Isaac Asimov", datetime(1920, 2, 1))
    greeneId = add_author(q, "Graham Greene", datetime(1904, 10, 2))
    pratchettId = add_author(q, "Terry Pratchett", datetime(1948, 4, 28))

    check(q.prepare, INSERT_GENRE_SQL)
    sfiction = add_genre(q, "Science Fiction")
    fiction = add_genre(q, "Fiction")
    fantasy = add_genre(q, "Fantasy")

    check(q.prepare, INSERT_BOOK_SQL)
    add_book(q, "Foundation", 1951, asimovId, sfiction, 3)
    add_book(q, "Foundation and Empire", 1952, asimovId, sfiction, 4)
    add_book(q, "Second Foundation", 1953, asimovId, sfiction, 3)
    add_book(q, "Foundation's Edge", 1982, asimovId, sfiction, 3)
    add_book(q, "Foundation and Earth", 1986, asimovId, sfiction, 4)
    add_book(q, "Prelude to Foundation", 1988, asimovId, sfiction, 3)
    add_book(q, "Forward the Foundation", 1993, asimovId, sfiction, 3)
    add_book(q, "The Power and the Glory", 1940, greeneId, fiction, 4)
    add_book(q, "The Third Man", 1950, greeneId, fiction, 5)
    add_book(q, "Our Man in Havana", 1958, greeneId, fiction, 4)
    add_book(q, "Guards! Guards!", 1989, pratchettId, fantasy, 3)
    add_book(q, "Night Watch", 2002, pratchettId, fantasy, 3)
    add_book(q, "Going Postal", 2004, pratchettId, fantasy, 3)
