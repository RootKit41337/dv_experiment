from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://www.youtube.com'),
            InlineKeyboardButton(text='Tg', url='tg://resolve?domain=hataHAMATURU')
        ]
    ]
)


sub_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Подписаться', url='https://t.me/fsoky_community'),
        ]
    ]
)