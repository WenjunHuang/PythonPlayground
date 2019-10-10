import asyncio
import itertools
import re
from collections import deque
from dataclasses import dataclass
from typing import Optional, Union, List
from os import path

from desktop.lib.git.merge import is_mergeheadset
from desktop.lib.models.repository import Repository


@dataclass
class StatusHeader:
    value: str


@dataclass
class StatusEntry:
    path: str
    status_code: str
    old_path: Optional[str]


StatusItem = Union[StatusHeader, StatusEntry]
kConflictStatusCode = ['DD', 'AU', 'UD', 'UA', 'DU', 'AA', 'UU']


async def get_status(repository: Repository):
    args = [
        'git',
        f"--git-dir {path.join(repository.path, '.git')}"
        '--no-optional-locks',
        'status',
        '--untracked-files=all',
        '--branch',
        '--porcelain=2',
        '-z',
    ]
    proc = await asyncio.create_subprocess_shell(' '.join(args),
                                                 stdout=asyncio.subprocess.PIPE,
                                                 stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()

    print(f'exited with {proc.returncode}')
    if stdout:
        parsed = parse_porcelain_status(stdout.decode())
        headers = itertools.takewhile(lambda i: type(i) == StatusItem, parsed)
        entries = itertools.takewhile(lambda i: type(i) == StatusEntry, parsed)
        merge_head_found = is_mergeheadset(repository)

        conflicted_files_in_index = itertools.takewhile(lambda i: i.status_code in kConflictStatusCode, entries)
        rebase_internal_state =
    if stderr:
        raise Exception(f'[stderr]\n{stderr.decode()}')


kChangeEntryType = '1'
kRenamedOrCopiedEntryType = '2'
kUnmergedEntryType = 'u'
kUntrackedEntryType = '?'
kIgnoredEntryType = '!'

kChangedEntryRe = re.compile(
    "^1 ([MADRCUTX?!.]{2}) (N\.\.\.|S[C.][M.][U.]) (\d+) (\d+) (\d+) ([a-f0-9]+) ([a-f0-9]+) ([\s\S]*?)$")


def parse_changed_entry(field: str) -> StatusEntry:
    match = kChangedEntryRe.match(field)
    if not match:
        raise Exception(f'Failed to parse status line for changed entry: ${field}')
    else:
        return StatusEntry(status_code=match[1], path=match[8])


kRenamedOrCopiedEntryRe = re.compile(
    "^2 ([MADRCUTX?!.]{2}) (N\.\.\.|S[C.][M.][U.]) (\d+) (\d+) (\d+) ([a-f0-9]+) ([a-f0-9]+) ([RC]\d+) ([\s\S]*?)$")


def parsed_renamed_or_copied_entry(field: str, old_path: Optional[str]) -> StatusEntry:
    match = kRenamedOrCopiedEntryRe.match(field)
    if not match:
        raise Exception(f'Failed to parse status line for renamed or copied entry: ${field}')
    else:
        if not old_path:
            raise Exception(f'Failed to parse renamed or copied entry, could not parse old path')
        return StatusEntry(status_code=match[1], old_path=old_path, path=match[9])


kUnmergedEntryRe = re.compile(
    "^u ([DAU]{2}) (N\.\.\.|S[C.][M.][U.]) (\d+) (\d+) (\d+) (\d+) ([a-f0-9]+) ([a-f0-9]+) ([a-f0-9]+) ([\s\S]*?)$")


def parse_unmerged_entry(field: str) -> StatusEntry:
    match = kUnmergedEntryRe.match(field)

    if not match:
        raise Exception(f"Failed to parse status line for unmerged entry: {field}")
    else:
        return StatusEntry(status_code=match[1], path=match[10])


def shift(queue: deque):
    try:
        left = queue.popleft()
    except IndexError:
        return None
    else:
        return left


def parse_porcelain_status(output: str) -> List[StatusItem]:
    tokens = output.split('\0')
    queue = deque(tokens)
    entries: List[StatusItem] = []

    field = shift(queue)

    while field:
        if field.startswith('# ') and len(field) > 2:
            entries.append(StatusHeader(value=field[2:]))
        else:
            entry_kind = field[0:1]
            if entry_kind == kChangeEntryType:
                entries.append(parse_changed_entry(field))
            elif entry_kind == kRenamedOrCopiedEntryType:
                entries.append(parsed_renamed_or_copied_entry(field, shift(queue)))
            elif entry_kind == kUnmergedEntryType:
                entries.append(parse_unmerged_entry(field))
            elif entry_kind == kIgnoredEntryType:
                pass

        field = shift(queue)
    return entries
