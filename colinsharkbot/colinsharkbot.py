from configparser import ConfigParser

from loguru import logger
from pyrogram import Client


class ColinSharkBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            session_name=name,
            workers=8,
            workdir=".",
            config_file=f"{name}.ini",
            plugins=dict(root=f"{name}.plugins", exclude=["welcome"]),
        )

    def start(self):
        super().start()
        logger.info("Bot Started | Logged in as " + self.get_me().username)

    def stop(self):
        super().stop()
        logger.info("Bot Stopped")
