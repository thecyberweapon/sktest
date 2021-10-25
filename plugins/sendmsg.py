import logging,os, requests
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client as Bot
from pyrogram import filters

chatid = os.environ.get("FORWARD_ID")
bot_token = os.environ.get("BOT_TOKEN")


async def sendmsg(text):
     #await Bot.send_message(chat_id=chatid,text=text)
     requests.get(url=f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chatid}&text={text}")
    
