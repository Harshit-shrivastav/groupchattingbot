import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters import Filter

CHAT_ID = int(os.environ.get("CHAT_ID", 0))
USER_ID = int(os.environ.get("USER_ID", 0))
BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

class IsPrivateUser(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == "private" and message.from_user.id == USER_ID

@dp.message(CommandStart(), IsPrivateUser())
async def cmd_start(message: Message):
    await message.answer("Hello👋\nNow send any message and it will be forwarded to your chat.")

@dp.message(IsPrivateUser())
async def handle_msg(message: Message):
    await bot.send_message(CHAT_ID, message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
