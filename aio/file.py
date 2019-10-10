import asyncio
from aiofile import AIOFile,Reader,Writer

async def main():
    async with AIOFile("/tmp/hello.txt",'w+') as afp:
        writer = Writer(afp)
        reader = Reader(afp,chunk_size=8)

        await writer("Hello")
        await writer(' ')
        await writer("World")
        await afp.fsync()

        async for chunk in reader:
            print(chunk)

asyncio.run(main())