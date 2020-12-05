from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Kotletki")
        ],
        [
            KeyboardButton(text='Makaroshki'),
            KeyboardButton(text="Kompotik"),
        ]
    ],
    resize_keyboard=True
)
