from dataclasses_json import dataclass_json, config
from dataclasses import dataclass, field
from abc import ABC
from urllib.parse import urlparse, urlsplit, urlunsplit
import re
from typing import *
from enum import Enum
from marshmallow import fields
import logging

import aiohttp
from .http import *


class GitHubAccountType(Enum):
    User = 'User'
    Organization = 'Organization'


def accounttype_decoder(value: str) -> GitHubAccountType:
    return GitHubAccountType(value)


@dataclass_json
@dataclass
class APIFullIdentityData:
    id: int
    url: str
    login: str
    avatar_url: str
    name: Optional[str] = None


@dataclass_json
@dataclass
class APIIdentityData:
    id: int
    url: str
    login: str
    avatar_url: str
    type: GitHubAccountType = field(
        metadata=config(
            encoder=GitHubAccountType,
            decoder=accounttype_decoder
        )
    )


@dataclass_json
@dataclass
class APIRepositoryData:
    clone_url: str
    ssh_url: str
    html_url: str
    name: str
    owner: APIIdentityData
    private: bool
    fork: bool
    default_branch: str
    pushed_at: str
    parent: Optional['APIRepositoryData'] = None


class IFetchAllOptions(ABC):
    def per_page(self) -> Optional[int]:
        pass

    def should_continue(self, result) -> bool:
        pass

    def next_page_path(self, response: aiohttp.ClientResponse) -> Optional[str]:
        pass

    def suppress_errors(self) -> bool:
        pass


def get_next_pagepath_from_link(response: aiohttp.ClientResponse) -> Optional[str]:
    '''Parses the link header from GitHub and returns the next path if one
        is present.
        If no link rel next header is found this method returns null.
    '''
    link_header = response.headers.get('Link')
    if not link_header:
        return None

    regex = re.compile('<([^>]+)>; rel="([^"]+)"')
    for part in link_header.split(','):
        match = regex.match(part.strip())
        if match and match[2] == 'next':
            t = urlsplit(match[1])
            next_url = urlunsplit(('', '', t.path, t.query, t.fragment))
            return next_url

    return None


class API:
    def __init__(self, session: aiohttp.ClientSession, endpoint: str, token: str):
        self.endpoint = endpoint
        self.token = token
        self.session = session

    async def fetch_repository(self, owner: str, name: str) -> Union[APIRepositoryData, None]:
        try:
            response = await self.request(HTTPMethod.GET,
                                          f'repos/{owner}/{name}')
            if response.status == 404:
                logging.warning(f'fetch_repository: "{owner}/{name}" return a 404')
                return None
            else:
                return await self.parse_response(response, APIRepositoryData)
        except Exception as e:
            logging.warning(f'fetch_repository: an error occured for "{owner}/{name}', e)
            return None

    async def fetch_repositories(self) -> Union[List[APIRepositoryData], None]:
        try:
            return await self.fetch_all("user/repos",
                                        APIRepositoryData)
        except Exception as e:
            logging.warning(f"fetch_repositories: {e}")
            return None

    async def fetch_account(self) -> APIFullIdentityData:
        try:
            response = await self.request(HTTPMethod.GET, 'user')
            return await self.parse_response(response, APIFullIdentityData)
        except Exception as e:
            logging.warning(f"fetch_account: failed with endpoint {self.endpoint}", e)

    async def fetch_all(self,
                        path: str,
                        cls,
                        options: Optional[IFetchAllOptions] = None):
        buf = []
        per_page = 100 if not options or not options.per_page() else options.per_page()
        next_path = url_with_query_string(path, per_page=str(per_page))

        while True:
            response = await self.request(HTTPMethod.GET, next_path)
            if response.status != 200 and (options and options.suppress_errors()):
                logging.warning(f"fetch_all: '{path}' returned a {response.status}")
                return buf

            items = await self.parse_response(response, cls, is_list=True)
            buf.extend(items)

            next_path = None if not options else options.next_page_path(response)
            next_path = get_next_pagepath_from_link(response) if not next_path else next_path

            if not next_path or (options and not options.should_continue(buf)):
                break

        return buf

    async def parse_response(self, response: aiohttp.ClientResponse, cls, is_list: bool = False):
        if response.status == 200:
            if not is_list:
                return await deserialize_object(response, cls)
            else:
                return await deserialize_list(response, cls)
        else:
            try:
                api_error = await deserialize_object(response, APIErrorData)
            except Exception as e:
                raise APIError(response, None)

            raise APIError(response, api_error)

    async def request(self,
                      method: HTTPMethod,
                      path: str,
                      body: Optional[Any] = None,
                      custom_headers: Optional[Mapping[str, str]] = None):
        return await request(self.session,
                             self.endpoint,
                             self.token,
                             method,
                             path,
                             body,
                             custom_headers)
