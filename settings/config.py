import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read .env variables
RESOURCES_FOLDER = os.environ.get("RESOURCES_FOLDER")
DRIVERS_FOLDER = os.environ.get("DRIVERS_FOLDER")
USER_MESSAGES_FOLDER = os.environ.get("USER_MESSAGES_FOLDER")
IMG_PATH = os.environ.get("IMG_PATH")
MESSAGES_FILE = os.environ.get("MESSAGES_FILE")
LOG_FILE = os.environ.get("LOG_FILE")
WHATSAPP_WEBPAGE = os.environ.get("WHATSAPP_WEBPAGE")
LOGGING_MESSAGE_FORMAT = os.environ.get("LOGGING_MESSAGE_FORMAT")
LOGGING_DATETIME_FORMAT = os.environ.get("LOGGING_DATETIME_FORMAT")

# Constants
SLEEP_TIME = 3

# Project absolute path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Create complete path
RESOURCES_PATH = join(PROJECT_DIR, RESOURCES_FOLDER)
USER_MESSAGES_PATH = join(RESOURCES_PATH, USER_MESSAGES_FOLDER)
DRIVER_PATH = join(RESOURCES_PATH, DRIVERS_FOLDER, "{sys_platform}")


class FileConf:

    class Paths:
        resources = RESOURCES_PATH
        user_messages = USER_MESSAGES_PATH
        img = IMG_PATH if IMG_PATH[0] == "/" else join(USER_MESSAGES_PATH, IMG_PATH)

    class FileNames:
        logger = join(PROJECT_DIR, LOG_FILE)
        messages = join(USER_MESSAGES_PATH, MESSAGES_FILE)
        chrome_driver = join(DRIVER_PATH, "chromedriver")


class LogConf:
    path = FileConf.FileNames.logger

    @staticmethod
    def create(logging):
        logging.basicConfig(
            format=LOGGING_MESSAGE_FORMAT,
            filename=LogConf.path,
            datefmt=LOGGING_DATETIME_FORMAT,
            level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.StreamHandler())
        return logger


class WhatsAppConfig:

    QR_ALT_STRING = "Scan me!"

    class XPATH:
        CHAT_NEW = "//div[@title='New chat']"
        CHAT_AVATAR = "//span[@title='%s']"
        BUTTON_TEXT_SEND = "//span[@data-icon='send']"
        BUTTON_ATTACH = "//div[@title='Attach']"
        BUTTON_FILE_INPUT = "//input[@type='file']"
        BUTTON_MEDIA_SEND = "//span[@data-icon='send-light']"
        INPUT_MESSAGE_BODY = "//div[@class='pluggable-input-body copyable-text selectable-text']"

    class ElementID:
        CHAT_LIST = "input-chatlist-search"
