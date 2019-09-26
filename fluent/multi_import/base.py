def foo_wrap(func):
    print(f'called foo_wrap for:{repr(func)}')
    return func
