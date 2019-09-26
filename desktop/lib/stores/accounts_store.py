import logging
import asyncio
from dataclasses import dataclass, asdict
from typing import *

from dataclasses_json import dataclass_json
from pyee import BaseEventEmitter

from desktop.lib.api import APIEmailData
from desktop.lib.auth import get_key_for_account
from desktop.lib.common import with_logger
from desktop.lib.models.account import Account, fetch_user
from desktop.lib.stores import IDataStore, ISecureStore
from .base_store import BaseStore


@dataclass_json
@dataclass
class AccountStore:
    token: str
    login: str
    endpoint: str
    emails: List[APIEmailData]
    avatar_url: str
    id: int
    name: str


@with_logger
class AccountsStore(BaseStore):
    def __init__(self, data_store: IDataStore, secure_store: ISecureStore):
        super().__init__()
        self._data_store = data_store
        self._security_store = secure_store
        self._emitter = BaseEventEmitter()
        self._loading_task = asyncio.create_task(self.__load_from_store())

    async def get_all(self) -> List[Account]:
        await self._loading_task
        return self._accounts.copy()

    async def add_account(self, account: Account) -> Optional[Account]:
        await self._loading_task

        updated = account
        try:
            updated = await updated_account(account)
        except Exception as e:
            self._logger.warning(f"Failed to fetch user {account.login}", e)

        try:
            await self._security_store.set_item(
                get_key_for_account(updated),
                updated.login,
                updated.token
            )
        except Exception as e:
            self._logger.error(f"Error adding account '{account.login}'", e)
            self.emit_error(e)
            return None

        self._accounts.append(updated)
        self.save()
        return updated

    async def __load_from_store(self):
        raw = self._data_store.get_item('users')
        if not raw:
            return

        accounts_with_tokens = []
        for item in map(lambda i: AccountStore.json.loads(i), raw):
            account_without_token = Account(**(asdict(item)))
            key = get_key_for_account(account_without_token)
            try:
                token = await self._security_store.get_item(key, item.login)
                accounts_with_tokens.append(account_without_token.with_token(token))
            except Exception as e:
                logging.error(f"Error getting token for '{key}'. Skipping.", e)
                self.emit_error(e)
        self._accounts = accounts_with_tokens
        self.emit_update(self._accounts)


async def updated_account(account: Account) -> Account:
    return await fetch_user(account.endpoint, account.token)
