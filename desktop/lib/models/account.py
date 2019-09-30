from dataclasses import dataclass, replace
from typing import List
import logging

from desktop.lib.api import APIEmailData, get_dotcom_api_endpoint, API, dataclass_json


@dataclass_json
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

    @staticmethod
    def anonymous() -> 'Account':
        return Account('', get_dotcom_api_endpoint(), '', [], '', -1, '')


async def fetch_user(endpoint: str, token: str) -> Account:
    api = API(endpoint, token)
    try:
        user = await api.fetch_account()
        emails = await api.fetch_emails()
        avatar_url = user.avatar_url
        return Account(user.login, endpoint, token, emails, avatar_url, user.id, user.name or user.login)
    except Exception as e:
        logging.getLogger(fetch_user.__name__).warning(f"failed with endpoint {endpoint}", e)
        raise e
