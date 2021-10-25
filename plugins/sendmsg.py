import logging
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client as Bot
from pyrogram import filters

chatid = os.environ.get("FORWARD_ID")


async def sendmsg(text):
     await Bot.send_message(chatid=chatid,text=text)
