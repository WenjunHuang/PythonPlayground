import asyncio


async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.create_task(set_after(fut, 1, '... world'))
    print('Hello ...')
    print(await fut)

asyncio.run(main())
