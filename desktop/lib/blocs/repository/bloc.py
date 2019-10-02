from typing import Any

from PyQt5.QtQml import QJSValue

from desktop.lib.api import API
from desktop.lib.bloc import Bloc
from desktop.lib.blocs.repository import RepositoryNotLoadedState, LoadAccountRepositoryEvent, \
    LoadingAccountRepositoriesState, FailToLoadAccountRepositoriesState, AccountRepositoriesLoadedState, Account


class AccountRepositoryBloc(Bloc):
    def __init__(self):
        super().__init__()

    def initial_state(self) -> Any:
        return RepositoryNotLoadedState()

    async def map_event_to_state(self, event):
        if isinstance(event, LoadAccountRepositoryEvent):
            yield LoadingAccountRepositoriesState(account=event.account)

            api = API(event.account.endpoint, event.account.token)
            try:
                repositories = await api.fetch_repositories()
            except Exception as e:
                yield FailToLoadAccountRepositoriesState(error=e)
            else:
                yield AccountRepositoriesLoadedState(account=event.account, repositories=repositories)

    def create_event(self, event_name: str, event_props: QJSValue):
        if event_name == LoadAccountRepositoryEvent.__name__:
            if event_props.isQObject():
                account = event_props.toQObject()
                if isinstance(account, Account):
                    return LoadAccountRepositoryEvent(account=account)
            raise Exception(f"event is not Account")

        return None
