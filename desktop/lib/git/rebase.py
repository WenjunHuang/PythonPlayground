from desktop.lib.models.repository import Repository
from os import path


def is_rebase_head_set(repository: Repository):
    p = path.join(repository.path, '.git', 'REBASE_HEAD')
    return path.exists(p)


async def get_rebase_internal_state(repository: Repository):
    is_rebase = is_rebase_head_set(repository)
    if not is_rebase:
        return None


