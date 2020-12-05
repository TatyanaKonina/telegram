from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer('Выберете товар из меню ниже', reply_markup=menu)


@dp.message_handler(text='Kotletki')
async def get_kotleltki(message: types.Message):
    await message.answer(f"Вы выбрали {message.text}")


@dp.message_handler(Text(equals=["Makaroshki", "Kompotik"]))
async def get_food(message: types.Message):
    await message.answer(f'Вы выбрали : {message.text}', reply_markup=ReplyKeyboardRemove())
