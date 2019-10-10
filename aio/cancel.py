import asyncio


async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    task = asyncio.create_task(cancel_me())

    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('main(): cancel_me is cancelled now')


asyncio.run(main())
