from aiogram import Bot, Dispatcher,types
from aiogram.utils import executor

bot = Bot(token='1451468048:AAG56RMeB1d4I3TYTuaLnR5ioV09Yb8IpYs')

dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message:types.Message):
    chat_id = message.chat.id
    # photo="https://yandex.ru/images/search?pos=0&img_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-zen_doc%2F1362253%2Fpub_5cf4d0bf6ba33d00afc8cc0b_5cf4d8eb9a90a100ae0543f2%2Fscale_1200&text=%D0%BA%D0%BE%D1%82%D0%B8%D0%BA&lr=47&rpt=simage&source=wiz"
    # send_photo = await bot.send_photo(chat_id=chat_id,photo=photo)
    # print(send_photo.photo[-1].file_unique_id)
    bot_user = await bot.get_me()
    print(bot_user.username)
executor.start_polling(dp)
