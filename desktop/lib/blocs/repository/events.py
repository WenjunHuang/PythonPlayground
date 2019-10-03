from abc import ABC
from dataclasses import dataclass

from desktop.lib.models import Account


@dataclass
class LoadAccountRepositoryEvent:
    pass
    # account: Account
