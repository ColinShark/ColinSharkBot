from base64 import b64decode
import requests
from textwrap import dedent

from pyrogram import filters
from pyrogram.types import Message

from ..colinsharkbot import ColinSharkBot

API = "https://api.mcsrvstat.us/2/"
ICON = "https://api.mcsrvstat.us/icon/"
TEXT = dedent("""
    [\u200C]({icon})__--**Minecraft Server**--__ - `{address}`
    Version: {version}
    Players: {pl_online}/{pl_max}
    Online: {players}
    Icon: ⬇️
""")

@ColinSharkBot.on_message(filters.command("mc", "#"))
def minecraft(bot: ColinSharkBot, message: Message):
    address = message.command[1] if len(message.command) > 1 else "pyrogram.org"
    reply = message.reply_text(f"`Looking up {address}`")

    r = requests.get(API + address)
    try:
        r.raise_for_status()
    except Exception as e:
        message.edit(message.text + "\n" + e)
        return
    r = r.json()

    if r["online"] == False:
        reply.edit_text(f"Server `{address}` is either invalid or offline.")
        return

    reply.edit_text(
        TEXT.format(
            address=address,
            version=r["version"],
            pl_online=r["players"]["online"],
            pl_max=r["players"]["max"],
            players=(
                ", ".join(
                    [
                        f"[{name}](https://namemc.com/profile/{name})"
                        for name
                        in r["players"]["list"]
                    ]
                )
            ) if "list" in r["players"] else "Nobody :(",
            icon=ICON + address
        )
    )
