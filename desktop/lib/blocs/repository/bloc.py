from typing import Any

from PyQt5.QtQml import QJSValue

from desktop.lib.api import API
from desktop.lib.bloc import Bloc, BlocError
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
            return LoadAccountRepositoryEvent.create(event_props)
        return None

    def dispatch(self, event_name: str, event_props: QJSValue):
        event = self.create_event(event_name, event_props)
        if event:
            asyncio.create_task(self.dispatch_event(event))
        else:
            raise BlocError(f"can not create event object of name: {event_name}")
