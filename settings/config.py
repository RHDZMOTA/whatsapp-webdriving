import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read .env variables
RESOURCES_FOLDER = os.environ.get("RESOURCES_FOLDER")
USER_MESSAGES_FOLDER = os.environ.get("USER_MESSAGES_FOLDER")
DRIVERS_FOLDER = os.environ.get("DRIVERS_FOLDER")
IMG_FOLDER = os.environ.get("IMG_FOLDER")
MESSAGES_FILE = os.environ.get("MESSAGES_FILE")
LOG_FILE = os.environ.get("LOG_FILE")

# Project absolute path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Create complete path
RESOURCES_PATH = join(PROJECT_DIR, RESOURCES_FOLDER)
USER_MESSAGES_PATH = join(RESOURCES_PATH, USER_MESSAGES_FOLDER)


class FileConf:

    class Paths:
        resources = RESOURCES_PATH
        user_messages = USER_MESSAGES_PATH
        img = join(USER_MESSAGES_PATH, IMG_FOLDER)

    class FileNames:
        logger = join(PROJECT_DIR, LOG_FILE)
        messages = join(USER_MESSAGES_PATH, MESSAGES_FILE)


class LogConf:
    path = FileConf.FileNames.logger
    format = '%(asctime)s %(levelname)s:%(message)s'
    datefmt = '%m/%d/%Y %I:%M:%S %p'

    @staticmethod
    def create(logging):
        logging.basicConfig(format=LogConf.format, filename=LogConf.path, datefmt=LogConf.datefmt, level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.StreamHandler())
        return logger


class WhatsAppConfig:

    QR_ALT_STRING = "Scan me!"

    class XPATH:
        CHAT_NEW = "//div[@title='New chat']"
        CHAT_AVATAR = "//div[@class='chat-avatar']"
        BUTTON_TEXT_SEND = "//button[@class='compose-btn-send']"
        BUTTON_ATTACH = "//div[@title='Attach']"
        BUTTON_FILE_INPUT = "//input[@type='file']"
        BUTTON_MEDIA_SEND = "//span[@data-icon='send-light']"
        INPUT_MESSAGE_BODY = "//div[@class='pluggable-input-body copyable-text selectable-text']"

    class ElementID:
        CHAT_LIST = "input-chatlist-search"
