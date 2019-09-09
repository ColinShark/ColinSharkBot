from configparser import ConfigParser

from loguru import logger
from pyrogram import Client


class TGbot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        config_file = f"{name}.ini"

        config = ConfigParser()
        config.read(config_file)

        super().__init__(
            session_name=name,
            bot_token=config.get(name, "bot_token"),
            workers=8,
            workdir=".",
            config_file=config_file,
            plugins=dict(root=f"{name}/plugins"),
        )

    def start(self):
        super().start()
        logger.info("Bot Started | Logged in as " + self.get_me().username)

    def stop(self):
        super().stop()
        logger.info("Bot Stopped")
