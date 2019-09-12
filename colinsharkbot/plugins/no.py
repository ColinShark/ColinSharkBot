import time

from pyrogram import Filters, Message, Emoji
from pyrogram.errors import FloodWait

from ..colinsharkbot import ColinSharkBot


@ColinSharkBot.on_message(Filters.command(["no", "no@ColinsharkBot"]))
def no(bot: ColinSharkBot, msg: Message):
    try:
        msg.reply_text("What did you expect to happen? " + Emoji.MAN_SHRUGGING)
    except FloodWait as e:
        time.sleep(e.x)
