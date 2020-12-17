import time

from pyrogram import filters, emoji
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from ..colinsharkbot import ColinSharkBot


@ColinSharkBot.on_message(filters.command(["no", "no@ColinsharkBot"]))
def no(bot: ColinSharkBot, msg: Message):
    try:
        msg.reply_text("What did you expect to happen? " + emoji.MAN_SHRUGGING)
    except FloodWait as e:
        time.sleep(e.x)
