import logging,os
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client as Bot
from pyrogram import filters
from main import validate,backgen
chatid = os.environ.get("FORWARD_ID")
    
#goat = False

'''
@Bot.on_message(filters.private)
async def backo(c,m):
   if not goat:
      asyncio.get_event_loop().create_task(backgen(c))
      goat=True
   await m.continue_propagation()
'''
@Bot.on_message(filters.private & filters.command(["start","help"]))
async def _start_cmd(bot,vishal):
    await vishal.reply("Hehe I can do many things that u can't do manually")

@Bot.on_message(filters.private & filters.command(["log"]))
async def _log_cmd(bot,vishal):
   try:
      await vishal.reply_document("logs/Log.txt")
   except Exception as e:
      await vishal.reply(f"Error\n{e}")

@Bot.on_message(filters.private & filters.command(["mstripe"]))
async def _mstr_cmd(bot, vishal):
    tex = vishal.text.replace("/mstripe ","")
    tex = tex.split("\n")
    for x in tex:
        validate(x.strip())
    await m.reply("Done vro")


