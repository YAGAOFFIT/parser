from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

chooseMainMenu = InlineKeyboardMarkup(row_width = 2)
chooseMainMenu.add(InlineKeyboardButton(text='Профиль', callback_data='btnAllReady'))\
            .insert(InlineKeyboardButton(text='Начать парсинг', callback_data='btnReturnBack'))