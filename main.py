#!/usr/bin/env python3
import time

from selenium import webdriver

from services.whatsapp import WhatsApp
from util import Messages, send_message

CHROME_DRIVER = "resources/drivers/linux/chromedriver"
SLEEP_TIME = 3


def main():
    driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=webdriver.ChromeOptions())
    whatsapp_service = WhatsApp(driver)
    message_service = Messages()
    for user in message_service.get_users():
        whatsapp_service.open_chat(user)
        time.sleep(SLEEP_TIME)
        messages = message_service.get_messages(user)
        for message in messages:
            send_message(whatsapp_service, message)
    whatsapp_service.close()


if __name__ == "__main__":
    main()
