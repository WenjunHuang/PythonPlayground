import sqlite3
from pypika import SQLLiteQuery as Query, Table, Field
from collections import namedtuple


def namedtuple_factory(cursor, row):
    fields = [col[0] for col in cursor.description]
    Row = namedtuple('Row', fields)
    return Row(*row)


with sqlite3.connect('example') as db:
    db.row_factory = namedtuple_factory
    customer = Table('t_customer')
    # q = Query.from_(customer).select(customer.id, customer.name, customer.description)
    q = Query.from_(customer).select('*')

    print(q.get_sql())
    cursor = db.execute(q.get_sql())
    data = cursor.fetchall()
    print(data)
    for i in data:
        print(i.name, i.description)

    q = Query.from_(customer) \
        .select(customer.id, customer.name, (customer.value2 - customer.value1)
                .as_('profit')).where(customer.name == '黄文俊')
    print(q.get_sql())
    cursor = db.execute(q.get_sql())
    data = cursor.fetchall()
    for i in data:
        print(i.name, i.profit)

    key_value = Table('t_key_value_string')
    replace = Query.into(key_value).columns(key_value.key, key_value.value).replace("abcd", "bcdd")
    cursor.execute(replace.get_sql())
