import unittest
import asyncio
from dataclasses import dataclass
from typing import *

from dataclasses_json import dataclass_json

from .api import API
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
    async def create_session(self):
        return aiohttp.ClientSession()

    async def get_result(self):
        async with aiohttp.ClientSession(json_serialize=json_dump) as session:
            response = await request(
                session,
                'http://192.168.2.243',
                None,
                HTTPMethod.GET,
                '/notification/backstage_audit/audit_notifications')
            result = await deserialize_object(response, PagingResult)
            return result

    def test_request(self):
        result = asyncio.run(self.get_result())
        # l = PagingResult.from_dict(result)
        # l = NotificationAudit.schema().load(result['data'], many=True)
        print(result)

    def test_fetch_repositories(self):
        loop = asyncio.get_event_loop()
        session = loop.run_until_complete(self.create_session())
        api = API(session, "https://api.github.com", "2fc514dec1b8ea0b7145b032ff0c81ed1c94fb4b")
        result = loop.run_until_complete(api.fetch_repositories())
        print(result)
        print(len(result))
        loop.close()

    def test_fetch_account(self):
        loop = asyncio.get_event_loop()
        session = loop.run_until_complete(self.create_session())
        api = API(session, "https://api.github.com", "2fc514dec1b8ea0b7145b032ff0c81ed1c94fb4b")
        result = loop.run_until_complete(api.fetch_account())
        print(result)
        loop.run_until_complete(session.close())
        loop.close()
