from enum import Enum, IntEnum,auto


class MyType(IntEnum):
    One = 1
    Two = auto()

print(MyType.Two.value)
