from pyrogram import Filters, Message, Emoji

from ..colinsharkbot import ColinSharkBot

MENTION = '<a href="tg://user?id={}">{}</a>'
MESSAGE = "Welcome to {}Pyrograms Lounge, {}"

@ColinSharkBot.on_message(Filters.new_chat_members & Filters.chat("pyrogramlounge"))
def welcome_people(bot: ColinSharkBot, msg: Message):
    new_members = [MENTION.format(x.id, x.first_name) for x in msg.new_chat_members]
    text = MESSAGE.format(Emoji.FIRE, " ".join(new_members))
    msg.reply_animation(
        animation="CgADAgADdQUAAleAoUsgGRxWRjl6_xYE",
        caption=text
    )
