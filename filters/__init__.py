from aiogram import Dispatcher

from .group_admin import IsAdmin
from .private_chat import IsPrivate
from .groups_chat import IsGroup

# Функция которая выполняет установку кастомных фильтров
def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate) # Устанавливаем кастомный фильтр на приватный чат с ботом
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsAdmin)