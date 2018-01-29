import time

from datetime import datetime

from settings import SLEEP_TIME


def send_message(whatsapp_service, message):
    if message.get("type") == "text":
        send_text_message(whatsapp_service, message)
        time.sleep(SLEEP_TIME)
    elif message.get("type") == "datetime-text":
        send_custom_message(whatsapp_service, message, {"datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        time.sleep(SLEEP_TIME)
    elif message.get("type") == "image":
        send_media_message(whatsapp_service, message)
        time.sleep(SLEEP_TIME)


def send_text_message(whatsapp_service, message):
    whatsapp_service.send_message_text(
        content=message.get("content"))


def send_media_message(whatsapp_service, message):
    whatsapp_service.send_message_media(
        media_path=message.get("path"),
        caption=message.get("caption")
    )


def send_custom_message(whatsapp_service, message, variables):
    whatsapp_service.send_message_text(
        content=message.get("content") % variables)
