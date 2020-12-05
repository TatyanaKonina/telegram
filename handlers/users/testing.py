from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Form


@dp.message_handler(Command("form"), state=None)
async def start_form(message: types.Message):

    await message.answer("Привет. Заполни, пожалуйста, форму!\n"
                         "Введите, пожалуйста, ваше имя\n")
    await Form.first()


@dp.message_handler(state=Form.name)
async def answer_name(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Name"] = answer
    await message.answer("Введите, пожалуйста, email\n")
    await Form.next()


@dp.message_handler(state=Form.email)
async def answer_email(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Email"] = answer
    await message.answer("Введите, пожалуйста, номер телефона\n")
    await Form.next()


@dp.message_handler(state=Form.phone_number)
async def answer_phone_number(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = message.text
    await message.answer(f"Привет! Ты ввел следующие данные\n"
                         f"Имя : {data.get('Name')}\n"
                         f"Email : {data.get('Email')}\n"
                         f"Телефон : {answer}")

    await state.finish()
    await state.reset_state(with_data=False)
    # await state.reset_state()
