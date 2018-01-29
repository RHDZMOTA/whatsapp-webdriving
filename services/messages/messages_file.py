import json

from services.messages import MessagesAbstract
from settings import FileConf


class MessagesFile(MessagesAbstract):

    def load_messages(self):
        self.messages = json.loads(open(FileConf.FileNames.messages, "r").read())

    def _get_ignored_users(self) -> list:
        return []

    def _get_users(self) -> list:
        return list(self.messages.keys())
