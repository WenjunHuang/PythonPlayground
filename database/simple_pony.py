import sqlite3
from pypika import Query, Table, Field
from collections import namedtuple


def namedtuple_factory(cursor, row):
    fields = [col[0] for col in cursor.description]
    Row = namedtuple('Row', fields)
    return Row(*row)


with sqlite3.connect('example') as db:
    db.row_factory = namedtuple_factory
    customer = Table('t_customer')
    q = Query.from_(customer).select(customer.id, customer.name, customer.description)

    print(q.get_sql())
    cursor = db.cursor()
    cursor.execute(q.get_sql())
    data = cursor.fetchall()
    print(data)

    q = Query.from_(customer) \
        .select(customer.id, customer.name, (customer.value2 - customer.value1)
                .as_('profit')).where(customer.name == '黄文俊')
    print(q.get_sql())
    cursor.execute(q.get_sql())
    data = cursor.fetchall()
    for i in data:
        print(i.name, i.profit)
