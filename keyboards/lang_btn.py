from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

lang_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('O\'zbekcha 🇺🇿'),
        ],
        [
            KeyboardButton('Русский 🇷🇺')
        ],
        [
            KeyboardButton('English 🇬🇧')
        ]

    ],
    resize_keyboard=True
)