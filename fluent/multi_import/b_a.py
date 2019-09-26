from a import a
from base import foo_wrap


@foo_wrap
def b():
    a()
    print('b called')
