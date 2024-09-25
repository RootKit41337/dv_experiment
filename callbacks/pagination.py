from contextlib import suppress
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import fabrics
from aiogram.exceptions import TelegramBadRequest
from data.subloader import get_json


router = Router()

smiles = [
    ["😦","Ни понял :_)"],
    ["🐵", "Ты макака"],
    [ "😒",  "Ну ёмаё"],
    ["😋", "Вкусняшка🤯"]
]

@router.callback_query(fabrics.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    page_n = int(callback_data.page)
    page = page_n - 1 if page_n > 0 else 0

    if callback_data.action == 'next':
        page = page_n + 1 if page_n < (len(smiles) - 1) else page_n 

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f'{smiles[page][0]} <b>{smiles[page][1]}</b>',
            reply_markup=fabrics.paginator(page)
        )
    await call.answer()