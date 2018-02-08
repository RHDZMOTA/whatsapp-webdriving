import os

from abc import ABCMeta, abstractmethod
from datetime import datetime

from services.whatsapp import WhatsApp
from settings import FileConf


class MessagesAbstract:
    __metaclass__ = ABCMeta

    def __init__(self, logger):
        self._logger = logger
        self._whatsapp_service = None
        self.messages = {}

    def set_whatsapp_service(self, whatsapp_service: WhatsApp):
        self._whatsapp_service = whatsapp_service

    def send_messages(self):
        ignored_users = self._get_ignored_users()

        for user in self._get_users():

            if user in ignored_users:
                self._logger.info("User %s ignored." % user)
                continue

            self._whatsapp_service.open_chat(user)
            messages = self._get_messages(user)

            for message in messages:
                self.send_message(message)

    def send_message(self, message: dict):
        if message.get("type") == "text":
            self.send_text_message(message)
        elif message.get("type") == "datetime-text":
            self.send_custom_message(message, {"datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        elif message.get("type") == "image":
            self.send_media_message(message)

    def send_text_message(self, message: dict):
        self._whatsapp_service.send_message_text(
            content=message.get("content"))

    def send_media_message(self, message: dict):
        self._whatsapp_service.send_message_media(
            media_path=os.path.join(FileConf.Paths.img, message.get("file_name")),
            caption=message.get("caption")
        )

    def send_custom_message(self, message: dict, variables: dict):
        self._whatsapp_service.send_message_text(
            content=message.get("content") % variables)

    def _get_messages(self, user) -> list:
        return self.messages.get(user)

    @abstractmethod
    def load_messages(self):
        pass

    @abstractmethod
    def _get_ignored_users(self) -> list:
        return []

    @abstractmethod
    def _get_users(self) -> list:
        return []
