import unittest
import asyncio
from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json

from .api import *
from .http import request, HTTPMethod, deserialize_object, json_dump
import aiohttp

T = TypeVar('T')


@dataclass_json
@dataclass
class NotificationAuditAttachment:
    attachment_id: str
    name: str
    uri: str


@dataclass_json
@dataclass
class NotificationAuditPicture:
    picture_id: str
    uri: str


@dataclass_json
@dataclass
class NotificationAuditUser:
    name: str
    phone: str
    school_name: str
    type_str: str
    user_id: str


@dataclass_json
@dataclass
class NotificationAudit:
    tag_str: str
    tag: str
    status: str
    resource_id: str
    content: str
    created: str
    user: NotificationAuditUser
    pictures: List[NotificationAuditPicture]
    attachments: List[NotificationAuditAttachment]


@dataclass_json
@dataclass
class PagingResult:
    total: int
    data: List[NotificationAudit]


class TestHttp(unittest.TestCase):
    def setUp(self) -> None:
        self.loop = asyncio.get_event_loop()
        self.session = self.loop.run_until_complete(self.create_session())
        self.token = '9c468038c7d20fe537086adf7a2e0fc496d6c177'
        self.endpoint = "https://api.github.com"

    def tearDown(self) -> None:
        self.loop.run_until_complete(self.session.close())
        self.loop.close()

    async def create_session(self):
        return aiohttp.ClientSession()

    async def get_result(self):
        response = await request(
            self.session,
            'http://192.168.2.243',
            None,
            HTTPMethod.GET,
            '/notification/backstage_audit/audit_notifications')
        result = await deserialize_object(response, PagingResult)
        return result

    def test_request(self):
        result = self.loop.run_until_complete(self.get_result())
        print(result)

    def test_fetch_repositories(self):
        api = API(self.session, "https://api.github.com", self.token)
        result = self.loop.run_until_complete(api.fetch_repositories())
        print(result)

    def test_fetch_account(self):
        api = API(self.session, "https://api.github.com", self.token)
        result = self.loop.run_until_complete(api.fetch_account())
        print(result)

    def test_fetch_emails(self):
        api = API(self.session, "https://api.github.com", self.token)
        result = self.loop.run_until_complete(api.fetch_emails())
        print(result)

    def test_fetch_commit(self):
        api = API(self.session, self.endpoint, self.token)
        result = self.loop.run_until_complete(
            api.fetch_commit('WenjunHuang', 'PythonPlayground', '28e0afd70bf79a4b53cbfc933dedfec838ad34d0'))
        print(result)

    def test_search_for_user_with_email(self):
        api = API(self.session, self.endpoint, self.token)
        result = self.loop.run_until_complete(
            api.search_for_user_with_email("tgrabiec@gmail.com"))
        print(result)

    def test_fetch_orgs(self):
        api = API(self.session, self.endpoint, self.token)
        result = self.loop.run_until_complete(
            api.fetch_orgs())
        print(result)

    def test_create_repository(self):
        api = API(self.session, self.endpoint, self.token)
        try:
            result = self.loop.run_until_complete(
                api.create_repository(None, "WenjunTestCreate", "WenjunTestCreate", False))
            print(result)
        except Exception as e:
            print(e)

    def test_fetch_issues(self):
        api = API(self.session, self.endpoint, self.token)
        result = self.loop.run_until_complete(
            api.fetch_issues("shiftkey", "desktop", IssueState.All))

        print(result)

    def test_fetch_all_open_pull_requests(self):
        api = API(self.session, self.endpoint, self.token)
        result = self.loop.run_until_complete(
            api.fetch_all_open_pull_requests("shiftkey", "desktop"))

        print(result)

    def test_fetch_protected_branches(self):
        api = API(self.session, self.endpoint, self.token)
        loop = asyncio.get_event_loop()
        task = loop.create_task(api.fetch_protected_branches("WenjunHuang", "WebFontendPlayground"))
        result = self.loop.run_until_complete(
            api.fetch_protected_branches("WenjunHuang", "WebFontendPlayground"))
        print(result)

        result = loop.run_until_complete(task)
        print(result)

