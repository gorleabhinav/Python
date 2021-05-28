import asyncio
import aiohttp
import aiofiles

async def data_request() -> None:
    """
    getting data from specified url
    """
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://python.org') as response:
                print("Status:", response.status)
        await asyncio.sleep(1)

async def read_file_content(file_name='tmp.txt',mode='r') -> None:
    """
    read content of the file
    """
    while True:
        async with aiofiles.open(file_name, mode) as f:
            contents = await f.read()
        print(contents)
        await asyncio.sleep(1)
    
async def dummy() -> None:
    print("hi i am dummy")
    await asyncio.sleep(0.5)

