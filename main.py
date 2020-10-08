"""Напишите простой скрипт для скачивания 10 файлов одновременно по HTTP"""
import asyncio
import aiohttp

def tasks():
    async def tsk(i):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://httpbin.org/get') as resp:
                f = open(f'/tmp/file{i}', 'wb')
                f.write(await resp.read())
                f.close()
    return [tsk(i) for i in range(10)]

async def main():
    await asyncio.gather(*tasks())


asyncio.run(main())

