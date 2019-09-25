from dataclasses import dataclass, replace
from typing import List

from desktop.lib.api import APIEmailData


@dataclass
class Account:
    login: str
    endpoint: str
    token: str
    emails: List[APIEmailData]
    avatar_url: str
    id: int
    name: str

    def with_token(self, token: str) -> 'Account':
        return replace(self, token=token)
