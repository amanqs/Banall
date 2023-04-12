import asyncio

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)


@bot.on_message(filters.command("banall", ["^", "-", "!", "x"]))
async def _(bot, msg):
    print(f"getting memebers from {msg.chat.id}")
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print(f"kicked {i.user.id} from {msg.chat.id}")
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(f" failed to kicked {i.user.id} from {e}")
    print("process completed")



@bot.on_message(filters.command("cek") & filters.private)
async def hello(bot, message):
    await message.reply("BAN ALL NYA HIDUP BANG AMANG")

