from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import game

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(game.router)

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))