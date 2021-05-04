
from loader import dp, bot
from aiogram.dispatcher.filters import Command
from aiogram import types

@dp.message_handler(Command("wall", prefixes="%^"), user_id=1184689415)
async def test(message: types.Message):
    await message.answer(message.text)