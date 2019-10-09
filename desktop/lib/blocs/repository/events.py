from dataclasses import dataclass
from typing import Optional

from PyQt5.QtQml import QJSValue


@dataclass
class LoadAccountRepositoryEvent:
    @classmethod
    def create(cls, js_props: Optional[QJSValue]):
        return LoadAccountRepositoryEvent()
