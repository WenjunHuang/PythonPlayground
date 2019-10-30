import asyncio
from asyncio.subprocess import PIPE


async def run():
    try:
        process = await asyncio.create_subprocess_exec("ls", stderr=PIPE, stdout=PIPE)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            print(process.returncode)
            msg = stderr.decode('utf-8')
            print(msg)
        else:
            msg = stdout.decode('utf-8')
            print(msg)
    except FileNotFoundError as e:
        print("file not found")


asyncio.run(run())
