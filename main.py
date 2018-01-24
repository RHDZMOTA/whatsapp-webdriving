#!/usr/bin/env python3
import logging
import time

from selenium import webdriver

from services.whatsapp import WhatsApp
from settings import LogConf
from util import Messages, send_message
from util.operative_system import select_driver

SLEEP_TIME = 3


def main(logger, ignore=[]):
    driver = webdriver.Chrome(select_driver(), chrome_options=webdriver.ChromeOptions())
    whatsapp_service = WhatsApp(driver)
    message_service = Messages()
    for user in message_service.get_users():
        if user in ignore:
            logger.info("User %s ignored." % user)
            continue
        whatsapp_service.open_chat(user)
        time.sleep(SLEEP_TIME)
        messages = message_service.get_messages(user)
        for message in messages:
            send_message(whatsapp_service, message)
            logger.info("Message send to user: %s." % user)
    whatsapp_service.close()


if __name__ == "__main__":
    logger = LogConf.create(logging)
    main(logger)
