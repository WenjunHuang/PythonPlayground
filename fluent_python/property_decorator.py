class Foo(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")


f = Foo("Guido")
n = f.name
f.name = "Monty"
try:
    f.name = 45
except TypeError as r:
    print("catcn type error in set an invalid value")

try:
    del f.name
except TypeError:
    print("can delete property name")
