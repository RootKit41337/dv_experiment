import os

from ujson import loads
import aiofiles


async def get_json(filename: str) -> list:
    path_1  = f'data/{filename}'
    if os.path.exists(path_1):
        async with aiofiles.open(path_1, 'r', encoding='utf-8') as file:
            return loads(await file.read())
    return []