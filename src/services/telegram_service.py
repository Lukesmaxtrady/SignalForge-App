from aiogram import Bot, Dispatcher, types

TELEGRAM_TOKEN = "your-telegram-bot-token"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def send_telegram_message(user_id: str, text: str):
    await bot.send_message(chat_id=user_id, text=text)
