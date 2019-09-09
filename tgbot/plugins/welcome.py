from pyrogram import Filters, Message, Emoji

from ..tgbot import TGbot

MENTION = '<a href="tg://user?id={}">{}</a>'
MESSAGE = "Welcome to {}Pyrograms Lounge{}, {}"

@TGbot.on_message(Filters.new_chat_members & Filters.chat("pyrogramlounge"))
def welcome_people(bot: TGbot, msg: Message):
    new_members = [MENTION.format(x.id, x.first_name) for x in msg.new_chat_members]
    text = MESSAGE.format(Emoji.FIRE, Emoji.COUCH_AND_LAMP, " ".join(new_members))
    msg.reply_animation(
        animation="CgADAgADdQUAAleAoUsgGRxWRjl6_xYE",
        caption=text
    )
