import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Siz yubordingiz:\n<code>{message.text}</code>")

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
