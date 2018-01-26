import json
import time

from settings import FileConf, SLEEP_TIME
from util.messages import send_message


class MessagesFile(object):

    def __init__(self, logger):
        self.messages = json.loads(open(FileConf.FileNames.messages, "r").read())
        self.logger = logger

    def get_users(self):
        return list(self.messages.keys())

    def get_messages(self, user):
        return self.messages.get(user)

    @staticmethod
    def get_ignored_users():
        return []  # TODO: read file.

    def send_messages(self, whatsapp_service):
        ignored_users = self.get_ignored_users()

        for user in self.get_users():

            if user in ignored_users:
                self.logger.info("User %s ignored." % user)
                continue

            whatsapp_service.open_chat(user)
            time.sleep(SLEEP_TIME)
            messages = self.get_messages(user)

            for message in messages:
                send_message(whatsapp_service, message)