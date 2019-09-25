import logging
import asyncio
from dataclasses import dataclass, asdict
from typing import *

from dataclasses_json import dataclass_json
from pyee import BaseEventEmitter

from desktop.lib.api import APIEmailData
from desktop.lib.auth import get_key_for_account
from desktop.lib.models.account import Account
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


class AccountsStore(BaseStore):
    def __init__(self, data_store: IDataStore, secure_store: ISecureStore):
        super().__init__()
        self._data_store = data_store
        self._security_store = secure_store
        self._emitter = BaseEventEmitter()
        asyncio.create_task(self.__load_from_store())

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
