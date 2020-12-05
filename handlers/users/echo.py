from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    chat_id = message.from_user.id
    text = message.text

    # from loader import bot

    # from aiogram import  Bot
    # bot = Bot.get_current()

    bot = dp.bot

    await message.answer(text=text)
    # await message.reply(text=text) ссылка на сообщение
    # await bot.send_message(chat_id=chat_id,text=text)

    # await message.answer(message.text)