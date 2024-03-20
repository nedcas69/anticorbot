from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards import lang_btn  # Импортируем нашу клавиатуру
from loader import dp


@dp.message_handler(Command("start"))  # Создаём message handler который ловит команду /menu
async def menu(message: types.Message):  # Создаём асинхронную функцию
    await message.answer("Выберите язык!", reply_markup=lang_btn)
