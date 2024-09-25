from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from keyboards.inline import sub_kb

class check_subs(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member("@fsoky_community", event.from_user.id)

        if chat_member.status == 'left':
            await event.answer(
                'Подпишись канал для продолжения!',
                reply_markup= sub_kb
            )
        else:
            return await handler(event, data)