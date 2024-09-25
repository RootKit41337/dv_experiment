from aiogram.types import (ReplyKeyboardMarkup,
KeyboardButton,
KeyboardButtonPollType,
ReplyKeyboardRemove)

main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Смайлики'),
            KeyboardButton(text='Ссылки')
        ], 
        [
            KeyboardButton(text='Калькулятор'),
            KeyboardButton(text='Спец. кнопки')
        ]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню',
    selective=True
)


sp_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить геопозицию', request_location=True),
            KeyboardButton(text='Отправить контакт', request_contact=True),
            KeyboardButton(text='Создать викторину или опрос', request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню',
    selective=True
)

rmk = ReplyKeyboardRemove()
