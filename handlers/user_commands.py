from aiogram import Router, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from aiogram.enums.dice_emoji import DiceEmoji


from keyboards import reply

from filters.is_admin import IsAdmin
from filters.is_digit_or_float import checkForDigit

router = Router()


@router.message(CommandStart()) #IsAdmin([1780609324])
async def start(message: Message):
    await message.answer(f'Hello, <strong>{message.from_user.first_name}</strong>', reply_markup=reply.main_kb)


@router.message(Command('pay'), checkForDigit()) #! /pay text == int or float
async def pay_the_order(message: Message, command: CommandObject) -> None:
    await message.answer(f'Вы успешно купили товар!')



@router.message(Command(commands=['rn', 'random-number']))
async def random(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split('-')]
    rnum = random.randint(a, b)
    await message.reply(f'Random number: {rnum}')


@router.message(Command(commands=['help', 'HELP', 'Help']))
async def help_command(message: Message):
    await message.answer(f'/start - перезагрузить бота \n/help - помощь \n/profile - твой профиль \n/random-number - рандомное число \n/pay - увидеть "вы купили товар" ')            

