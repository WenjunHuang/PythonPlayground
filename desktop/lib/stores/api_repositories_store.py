from dataclasses import dataclass, replace
from typing import List, Mapping, Optional, Tuple

from desktop.lib.api import APIRepositoryData, API
from desktop.lib.models.account import Account
from desktop.lib.stores.accounts_store import AccountsStore
from desktop.lib.stores.base_store import BaseStore


@dataclass
class AccountRepositories:
    repositories: List[APIRepositoryData]
    loading: bool


class ApiRepositoriesStore(BaseStore):
    _account_state: List[Tuple[Account, AccountRepositories]]

    def __init__(self, accounts_store: AccountsStore):
        super().__init__()
        self._account_state = []
        accounts_store.update.connect(self.__on_accounts_changed)

    async def load_repositories(self, account: Account):
        existing_account = resolve_account(account, self._account_state)
        existing_repositories = None
        for a, r in self._account_state:
            if a == existing_account:
                existing_repositories = r
                break

        if existing_repositories and existing_repositories.loading:
            return

        self.__update_account(existing_account, loading=True)
        api = API(existing_account.endpoint, existing_account.token)
        repositories = await api.fetch_repositories()

        if not repositories:
            self.__update_account(account, loading=False)
        else:
            self.__update_account(account, loading=False, repositories=repositories)

    def get_state(self):
        return self._account_state

    def __update_account(self, account: Account, *, loading: Optional[bool] = None,
                         repositories: Optional[List[APIRepositoryData]] = None):
        new_state = list(self._account_state)
        newOrExistingAccount = resolve_account(account, new_state)
        existing_repositories = None
        for a, v in new_state:
            if a == newOrExistingAccount:
                existing_repositories = v
                break
        else:
            existing_repositories = AccountRepositories(loading=False,
                                                        repositories=[])

        update = {}
        if loading:
            update['loading'] = loading
        if repositories:
            update['repositories'] = repositories
        new_repositories = replace(existing_repositories, **update)
        new_state[newOrExistingAccount] = new_repositories
        self._account_state = new_state
        self.emit_update(self._account_state)

    def __on_accounts_changed(self, accounts: List[Account]):
        new_state = {}
        for account in accounts:
            for key, value in self._account_state.items():
                if account_equals(key, account):
                    new_state[account] = value
                    break

        self._account_state = new_state
        self.emit_update(self._account_state)


def account_equals(x: Account, y: Account) -> bool:
    return x.endpoint == y.endpoint and x.id == y.id


def resolve_account(account: Account,
                    account_state: List[Tuple[Account, AccountRepositories]]):
    for k, _ in account_state:
        if account == k:
            return account

    for existing_account, _ in account_state:
        if account_equals(existing_account, account):
            return existing_account
    return account
