from dataclasses import dataclass
from typing import List

from desktop.lib.api import APIRepositoryData
from desktop.lib.models import Account


class RepositoryState:
    pass


class RepositoryNotLoadedState(RepositoryState):
    pass


@dataclass
class LoadingAccountRepositoriesState(RepositoryState):
    account: Account


@dataclass
class AccountRepositoriesLoadedState(RepositoryState):
    account: Account
    repositories: List[APIRepositoryData]


@dataclass
class FailToLoadAccountRepositoriesState(RepositoryState):
    error: Exception
