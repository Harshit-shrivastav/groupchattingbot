# Author: pyrogrammers (https://github.com/pyrogrammers) (@pyrogrammers)
import os
from pyrogram import Client, filters
CHAT_ID = int(os.environ.get("CHAT_ID", 0))
USER_ID = int(os.environ.get("USER_ID", 0))
Bot = Client(
    "Group-chatting-bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
@Bot.on_message(filters.private & filters.all & filters.user(USER_ID))
async def start(bot, update):
    await bot.send_message(CHAT_ID,update.text)
Bot.run()
