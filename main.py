import asyncio
from aiogram import Bot, Dispatcher
from handlers import bot_messages, user_commands, quest
from callbacks import pagination

# from config_rider import config

# from middlewares.check_sub import check_subs

async def main():
    bot = Bot('6791278386:AAFX-2SQUU7oaTLQ23nzIiDJHpflHco8mas', parse_mode='HTML')
    dp = Dispatcher()

    # dp.message.middleware(check_subs())

    dp.include_routers(
        user_commands.router, 
        pagination.router,
        quest.router,
        bot_messages.router
    )

    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
