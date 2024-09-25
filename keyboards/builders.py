from aiogram.utils.keyboard import ReplyKeyboardBuilder


def calc():
    items = [
        '1', '2', '3', '/',
        '4', '5', '6', '*',
        '7', '8', '9', '-',
        '0', '.', '=', '+',
    ]

    bulder = ReplyKeyboardBuilder()
    [bulder.button(text=item) for item in items]
    bulder.button(text='Назад')
    bulder.adjust(4,4,4,4,1)

    return bulder.as_markup(resize_keyboard=True)


def profile(text: str | list):
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)