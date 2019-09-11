import asyncio
from aiohttp import ClientSession
from typing import Any
from bs4 import BeautifulSoup


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    resp = await session.request(method='GET', url=url, **kwargs)
    resp.raise_for_status()
    html = await resp.text()
    return html


async def parse(html: str) -> Any:
    return BeautifulSoup(html)


async def main():
    bsObj = None
    async with ClientSession() as session:
        html = await fetch_html('http://www.pythonscraping.com/pages/page3.html', session)
        bsObj = await parse(html)

    for child in bsObj.find("table",{"id":"giftList"}).children:
        print(child)



asyncio.run(main())
