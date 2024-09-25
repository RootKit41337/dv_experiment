from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from keyboards import inline, reply, builders, fabrics
from data.subloader import get_json



router = Router()
smiles = [
        ["😦","Ни понял :_)"],
        ["🐵", "Ты макака"],
        [ "😒",  "Ну ёмаё"],
        ["😋", "Вкусняшка🤯"]
]

@router.message(F.text.lower().in_(['Привет', 'хай', 'Hello']))
async def hello(message: Message):
    await message.reply('Привеееееееееееееееееееееееееееееееееееееет!')

@router.message()
async def sil(message: Message):
    msg = message.text.lower()

    if msg == 'ссылки':
        await message.answer('Вот ваши ссылки', reply_markup=inline.lin_kb)
    elif msg == 'cпец. кнопки':
        await message.answer(f'Спец. кнопки', reply_markup=reply.sp_kb)
    elif msg == 'калькулятор':
        await message.answer(f'Вот ваш калькулятор', reply_markup=builders.calc())
    elif msg == 'смайлики':
        await message.answer(f'{smiles[0][0]} <b>{smiles[0][1]}</b>', reply_markup=fabrics.paginator())