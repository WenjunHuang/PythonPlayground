from dataclasses import dataclass

# A github repository
from typing import Optional

from desktop.lib.models.owner import Owner


@dataclass
class GitHubRepository:
    db_id: Optional[int]
    name: str
    owner: Owner
    private: Optional[bool]
    html_url: Optional[str]
    default_branch: Optional[str]
    clone_url: Optional[str]
    parent: Optional['GitHubRepository']

    def endpoint(self):
        return self.owner.endpoint

    def full_name(self):
        return f'{self.owner.login}/{self.name}'

    def fork(self):
        if not self.parent:
            return True
        else:
            return False
