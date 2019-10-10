import asyncio
from aiohttp import request
from aiomultiprocess import Worker


async def put(url, params):
    async with request('PUT', url, params=params) as response:
        return await response.text('utf-8')


async def main():
    p = Worker(target=put, args=("https://jreese.sh", {}))
    response = await p
    print(response)


asyncio.run(main())
