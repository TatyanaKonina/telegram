from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестированиею\n"
                         "Вы часто занимаетесь бессмысленными делами?\n")


#   await Test.q1.set()
    await Test.first()


@dp.message_handler(state=Test.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    # await state.update_data(answer1=answer)
    # await state.update_data(
    #     {
    #         "answer1" : answer
    #     }
    # )
    async with state.proxy() as data:
        data["answer1"] = answer
    await message.answer("Вопрос 2\n"
                         "Вы часто сидите в интаграмме?\n")
    await Test.next()
    # await Test.q2.set()
@dp.message_handler(state=Test.q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text
    await message.answer(f"Спасибо за ваши ответы:\n"
                         f"Ответ 1 : {answer1}\n"
                         f"Ответ 2 : {answer2}")

    # await state.finish()
    # await state.reset_state()