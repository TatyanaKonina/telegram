from aiogram import types
from loader import dp
from pathlib import Path


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def download_document(message: types.Message):
    path_to_download = Path().joinpath("items", "categories", "subcategories", "photos")
    path_to_download.mkdir(parents=True, exist_ok=True)
    # print(message.photo[-1])

    path_to_download = path_to_download.joinpath('photo.jpg')
    await message.photo[-1].download(destination=path_to_download)
    await message.answer(f"Документ был сохранен в путь: {path_to_download}")