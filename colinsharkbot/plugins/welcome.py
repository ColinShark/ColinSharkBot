from pyrogram import filters, emoji
from pyrogram.types import Message

from ..colinsharkbot import ColinSharkBot


# Dan didn't want welcome bots anymore :(
@ColinSharkBot.on_message(filters.new_chat_members & filters.chat("pyrogramlounge"))
def welcome_people(bot: ColinSharkBot, msg: Message):
    new_members = [u.mention for u in msg.new_chat_members]
    text = f"Welcome to {emoji.FIRE}Pyrograms Lounge, {', '.join(new_members)}"

    msg.reply_animation(animation="CgADAgADdQUAAleAoUsgGRxWRjl6_xYE", caption=text)
