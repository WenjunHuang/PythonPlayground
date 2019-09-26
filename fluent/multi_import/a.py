from base import foo_wrap
from b_a import b


@foo_wrap
def a():
    print('a called')
