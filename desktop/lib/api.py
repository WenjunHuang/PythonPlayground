from dataclasses_json import dataclass_json, config
from dataclasses import dataclass, field
from abc import ABC
from urllib.parse import urlparse, urlsplit, urlunsplit, unquote
import re
from typing import *
from enum import Enum
from marshmallow import fields
import logging
from datetime import datetime
import math

import aiohttp
from .http import *


class GitHubAccountType(Enum):
    User = 'User'
    Organization = 'Organization'

    @classmethod
    def from_str(cls, value: str) -> 'GitHubAccountType':
        return GitHubAccountType(value)


class IssueState(Enum):
    Open = 'open'
    Closed = 'closed'
    All = 'all'

    @classmethod
    def from_str(cls, value: str) -> 'IssueState':
        return IssueState(value)


@dataclass_json
@dataclass
class APIIssueData:
    number: int
    title: str
    state: IssueState = field(
        metadata=config(
            encoder=IssueState,
            decoder=IssueState.from_str
        )
    )
    updated_at: str
    pullRequest: Optional[bool] = None
    # pull_request: bool


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
            decoder=GitHubAccountType.from_str
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


class EmailVisibility(Enum):
    Public = 'public'
    Private = 'private'

    @classmethod
    def from_str(cls, value: str):
        if not str:
            return None
        return EmailVisibility(value)


@dataclass_json
@dataclass
class APIEmailData:
    email: str
    verified: bool
    primary: bool
    visibility: Optional[EmailVisibility] = field(
        metadata=config(
            encoder=EmailVisibility,
            decoder=EmailVisibility.from_str
        )
    )


@dataclass_json
@dataclass
class APISearchForUsersResults:
    items: List[APIIdentityData]


@dataclass_json
@dataclass
class APICommitData:
    sha: str
    author: Optional[APIIdentityData] = None


@dataclass_json
@dataclass
class APIOrganizationData:
    id: int
    url: str
    login: str
    avatar_url: str


class PullRequestState(Enum):
    Open = 'open'
    Closed = 'closed'

    @classmethod
    def from_str(cls, value: str) -> 'PullRequestState':
        return PullRequestState(value)


@dataclass_json
@dataclass
class APIPullRequestRefData:
    ref: str
    sha: str


@dataclass_json
@dataclass
class APIPullRequestData:
    number: int
    title: str
    created_at: str
    updated_at: str
    user: APIIdentityData
    base: APIPullRequestRefData
    head: APIPullRequestRefData
    state: PullRequestState = field(
        metadata=config(
            encoder=PullRequestState,
            decoder=PullRequestState.from_str
        )
    )


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


def to_github_iso_datestring(time: datetime) -> str:
    return time.isoformat(timespec='seconds')


class API:
    def __init__(self, session: aiohttp.ClientSession, endpoint: str, token: str):
        self.endpoint = endpoint
        self.token = token
        self.session = session

    async def fetch_repository(self, owner: str, name: str) -> Union[APIRepositoryData, None]:
        try:
            response = await self.__request(HTTPMethod.GET,
                                            f'repos/{owner}/{name}')
            if response.status == 404:
                logging.warning(f'fetch_repository: "{owner}/{name}" return a 404')
                return None
            else:
                return await self.__parse_response(response, APIRepositoryData)
        except Exception as e:
            logging.warning(f'fetch_repository: an error occured for "{owner}/{name}', e)
            return None

    async def fetch_repositories(self) -> Union[List[APIRepositoryData], None]:
        try:
            return await self.__fetch_all("user/repos",
                                          APIRepositoryData)
        except Exception as e:
            logging.warning(f"fetch_repositories: {e}")
            return None

    async def fetch_account(self) -> APIFullIdentityData:
        try:
            response = await self.__request(HTTPMethod.GET, 'user')
            return await self.__parse_response(response, APIFullIdentityData)
        except Exception as e:
            logging.warning(f"fetch_account: failed with endpoint {self.endpoint}", e)

    async def fetch_emails(self) -> List[APIEmailData]:
        try:
            response = await self.__request(HTTPMethod.GET, 'user/emails')
            return await self.__parse_response(response, APIEmailData, is_list=True)
        except Exception as e:
            logging.warning(f"fetch_emails: failed with endpoint {self.endpoint}", e)
            return []

    async def fetch_commit(self, owner: str, name: str, sha: str) -> Optional[APICommitData]:
        try:
            path = f"repos/{owner}/{name}/commits/{sha}"
            response = await self.__request(HTTPMethod.GET, path)
            if response.status == 404:
                logging.warning(f"fetch_commit: '{path}' returned a 404")
                return None
            return await self.__parse_response(response, APICommitData)
        except Exception as e:
            logging.warning(f"fetch_commit: returned an error '{owner}/{name}@{sha}'", e)
            return None

    async def search_for_user_with_email(self, email: str) -> Optional[APIIdentityData]:
        if not email:
            return None
        try:
            url = url_with_query_string('search/users', q=f"{email} in:email type:user")
            response = await self.__request(HTTPMethod.GET, url)
            result = await self.__parse_response(response, APISearchForUsersResults)
            items = result.items
            if len(items) > 0:
                return items[0]
            else:
                return None
        except Exception as e:
            logging.warning(f"search_for_user_with_email: not found '{email}'", e)
            return None

    async def fetch_orgs(self) -> List[APIOrganizationData]:
        try:
            return await self.__fetch_all('user/orgs', APIOrganizationData)
        except Exception as e:
            logging.warning(f"fetch_orgs: failed with endpoint {self.endpoint}", e)
            return []

    async def create_repository(self, org: Optional[APIOrganizationData],
                                name: str,
                                description: str,
                                private: bool) -> APIRepositoryData:
        try:
            api_path = f"orgs/{org.login}/repos" if org else 'user/repos'
            response = await self.__request(HTTPMethod.POST,
                                            api_path, {
                                                'name': name,
                                                'description': description,
                                                'private': private
                                            })
            return await self.__parse_response(response, APIRepositoryData)
        except APIError as e:
            if org:
                raise Exception(
                    f"Unable to create repository for organization {org.login}. Verify that it exists, that it's a paid organization, and that you have permission to create a repository there.")
            raise e
        except Exception as e:
            logging.warning(f"create_repository: failed with endpoint {self.endpoint}", e)
            raise Exception(
                "Unable to publish repository.Please check if you have an internet connection and try again. ")

    async def fetch_issues(self, owner: str, name: str, state: IssueState, since: Optional[datetime] = None) -> \
            Iterable[
                APIIssueData]:
        params = {'state': state.value}
        if since:
            params['since'] = to_github_iso_datestring(since)

        url = url_with_query_string(f"repos/{owner}/{name}/issues", **params)
        try:
            issues = await self.__fetch_all(url, APIIssueData)
            return list(filter(lambda i: not i.pullRequest, issues))
        except Exception as e:
            logging.warning(f"fetch_issues: failed for repository {owner}/{name}", e)
            raise e

    async def fetch_all_open_pull_requests(self, owner: str, name: str) -> List[APIPullRequestData]:
        url = url_with_query_string(f"repos/{owner}/{name}/pulls", state='open')
        try:
            return await self.__fetch_all(url, APIPullRequestData)
        except Exception as e:
            logging.warning(f"failed fetching open PRs for repository {owner}/{name}", e)
            raise e

    async def fetch_updated_pull_requests(self, owner: str, name: str, since: datetime, max_results: int = 320):
        url = url_with_query_string(f"repos/{owner}/{name}/pulls", state='all', sort='updated', direction='desc')
        try:
            prs = await self.__fetch_all(url, APIPullRequestData, )

    async def __fetch_all(self,
                          path: str,
                          cls,
                          options: Optional[IFetchAllOptions] = None) -> List:
        buf = []
        per_page = 100 if not options or not options.per_page() else options.per_page()
        next_path = url_with_query_string(path, per_page=str(per_page))

        while True:
            response = await self.__request(HTTPMethod.GET, next_path)
            if response.status != 200 and (options and options.suppress_errors()):
                logging.warning(f"fetch_all: '{path}' returned a {response.status}")
                return buf

            items = await self.__parse_response(response, cls, is_list=True)
            buf.extend(items)

            next_path = None if not options else options.next_page_path(response)
            next_path = get_next_pagepath_from_link(response) if not next_path else next_path

            if not next_path or (options and not options.should_continue(buf)):
                break

        return buf

    async def __parse_response(self, response: aiohttp.ClientResponse, cls, is_list: bool = False):
        if response.status == 200 or response.status == 201:
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

    async def __request(self,
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


class FetchUpdatedPullRequestOpt(IFetchAllOptions):
    def per_page(self) -> Optional[int]:
        return 10

    def next_page_path(self, response: aiohttp.ClientResponse) -> Optional[str]:
        next_path = get_next_pagepath_from_link(response)
        if not next_path:
            return None

        query_str = urlsplit(next_path).query
        query_list = [sub.partition('=') for sub in query_str.split('&')]
        query_dict = {left: unquote(right) for (left, _, right) in query_list}

        page_size = int(query_dict.get('per_page'), 10) if 'per_page' in query_dict else None
        page_number = int(query_dict.get('page'), 10) if 'page' in query_dict else None

        if not page_size or not page_number:
            return next_path

        current_page = page_number - 1
        received = current_page * page_size
        next_page_size = min(100, page_size * 2)

        if page_size != next_page_size and received % next_page_size == 0:
