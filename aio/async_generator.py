import asyncio
from asyncio import Task

from aiohttp import ClientSession
from dataclasses import dataclass


class Event:
    pass


@dataclass
class GetContentEvent(Event):
    url: str


class State:
    pass


@dataclass
class StartGetContentState(State):
    url: str


@dataclass
class SuccessGetContentState(State):
    url: str
    result: str


@dataclass
class FailGetContentState(State):
    url: str
    error: str


async def map_event_to_state(event):
    if isinstance(event, GetContentEvent):
        yield StartGetContentState(url=event.url)

        async with ClientSession() as session:
            async with session.get(event.url) as response:
                if response.status == 200:
                    content = await response.text()
                    yield SuccessGetContentState(url=event.url, result=content)
                else:
                    yield FailGetContentState(url=event.url, error=f"status:{response.status}")


def transform_events(queue: asyncio.Queue) -> (Task, asyncio.Queue):
    states = asyncio.Queue()

    async def worker():
        while True:
            event = await queue.get()
            async for state in map_event_to_state(event):
                await states.put(state)

            queue.task_done()

    task = asyncio.create_task(worker())

    return task, states


async def state_listener(queue: asyncio.Queue):
    while True:
        state = await queue.get()
        queue.task_done()

        print(state)


async def test():
    event_queue = asyncio.Queue()
    event_task, state_queue = transform_events(event_queue)
    state_task = asyncio.create_task(state_listener(state_queue))

    await event_queue.put(GetContentEvent(url="https://news.sina.com.cn"))
    await event_queue.put(GetContentEvent(url="https://www.bilibili.com/"))

    await event_queue.join()
    await state_queue.join()

    tasks = [event_task, state_task]
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(test())

finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
