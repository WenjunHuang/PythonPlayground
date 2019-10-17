from dataclasses import dataclass, field
from typing_extensions import Literal
from enum import Enum


class FooType(Enum):
    One = "One"
    Two = "Two"


@dataclass(frozen=True)
class B:
    kind: FooType


@dataclass(frozen=True)
class D(B):
    kind: Literal[FooType.One] = field(init=False, default=FooType.One)
    address: str


d = D(address='guangzhou')
print(d.kind.value)
