import aiohttp as http
import asyncio



async def simple_get():
    session = http.ClientSession()
    params = [('key','value1'),('key','value2')]
    async with session.get("http://httpbin.org/get", params=params) as resp:
        print(resp.url)

    await session.close()

asyncio.run(simple_get())
