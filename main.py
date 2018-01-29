#!/usr/bin/env python3
import logging

from selenium import webdriver

from settings import LogConf
from services.messages import MessagesFile
from services.whatsapp import WhatsApp
from util.operative_system import select_driver

logger = LogConf.create(logging)


def main():

    driver = webdriver.Chrome(select_driver(), chrome_options=webdriver.ChromeOptions())

    whatsapp_service = WhatsApp(driver=driver, logger=logger)
    whatsapp_service.initialize_session()

    message_service = MessagesFile(logger=logger)
    message_service.set_whatsapp_service(whatsapp_service=whatsapp_service)
    message_service.load_messages()
    message_service.send_messages()

    whatsapp_service.close()


if __name__ == "__main__":
    main()
