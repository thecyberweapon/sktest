import logging
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client as Bot
from pyrogram import filters


@Bot.on_message(filters.private & filters.command(["start","help"]))
async def _start_cmd(bot,vishal):
    await vishal.reply("Hehe I can do many things that u can't do manually")

@Bot.on_message(filters.private & filters.command(["log"]))
async def _log_cmd(bot,vishal):
   try:
      await vishal.reply_document("logs/Logs.txt")
   except Exception as e:
      await vishal.reply(f"Error\n{e}")
