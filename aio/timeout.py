import asyncio

async def eternity():
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    try:
        await asyncio.wait_for(eternity(),timeout = 1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())