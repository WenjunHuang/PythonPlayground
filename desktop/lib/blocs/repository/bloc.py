from typing import Any

from PyQt5.QtQml import QJSValue

from desktop.lib.api import API
from desktop.lib.bloc import Bloc
from desktop.lib.blocs.repository import RepositoryNotLoadedState, LoadAccountRepositoryEvent, \
    LoadingAccountRepositoriesState, FailToLoadAccountRepositoriesState, AccountRepositoriesLoadedState, Account
import asyncio


class AccountRepositoryBloc(Bloc):
    def __init__(self):
        super().__init__()

    def initial_state(self) -> Any:
        return RepositoryNotLoadedState()

    async def map_event_to_state(self, event):
        if isinstance(event, LoadAccountRepositoryEvent):
            yield LoadingAccountRepositoriesState()
            token = 'c415e9d535a95a28ecf955c01487330ebfa646e7'
            endpoint = "https://api.github.com"
            api = API(endpoint, token)
            try:
                repositories = await api.fetch_repositories()
            except Exception as e:
                yield FailToLoadAccountRepositoriesState(error=str(e))
            else:
                yield AccountRepositoriesLoadedState(repositories=repositories)

    def create_event(self, event_name: str, event_props: QJSValue):
        if event_name == LoadAccountRepositoryEvent.__name__:
            return LoadAccountRepositoryEvent()
            # if event_props.isQObject():
            # account = event_props.toQObject()
            # if isinstance(account, Account):
            # return LoadAccountRepositoryEvent(account=account)
            # raise Exception(f"event is not Account")

        return None

    def dispatch(self, event_name: str, event_props: QJSValue):
        event = self.create_event(event_name, event_props)
        asyncio.create_task(self.dispatch_event(event))
