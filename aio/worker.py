import asyncio
from aiohttp import request
from aiomultiprocess import Worker


async def get(url):
    async with request("GET", url) as response:
        return await response.text('utf-8')


async def worker_main():
    p = Worker(target=get, args=("https://jreese.sh", {}))
    response = await p


asyncio.run(worker_main())
