from abc import ABC
from dataclasses import dataclass

from desktop.lib.models import Account


class RepositoryEvent(ABC):
    pass


@dataclass
class LoadAccountRepositoryEvent(RepositoryEvent):
    account: Account
