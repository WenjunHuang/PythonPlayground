import asyncio
from aiofile import AIOFile, LineReader, Writer
import os


async def reader(fname):
    print('Start reader')
    async with AIOFile(fname, 'a') as afp:
        print('Begin read')
        while True:
            data = await afp.read(4096)
            print(data)


async def writer(fname):
    print('Start writer')
    async with AIOFile(fname, 'w') as afp:
        loop = asyncio.get_running_loop()
        while True:
            await asyncio.sleep(1)
            print('Begin write')
            await afp.write('%06f' % loop.time())


async def main():
    fifo_name = '/tmp/test.fifo'

    if os.path.exists(fifo_name):
        os.remove(fifo_name)

    os.mkfifo(fifo_name)

    await asyncio.gather(
        reader(fifo_name),
        reader(fifo_name),
        writer(fifo_name),
    )


asyncio.run(main())
