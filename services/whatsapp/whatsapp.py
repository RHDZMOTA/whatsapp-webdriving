import time

from settings import SLEEP_TIME, INITIAL_SLEEP_TIME, WHATSAPP_WEBPAGE
from settings.config import WhatsAppConfig


class WhatsApp(object):

    def __init__(self, driver, logger):
        self.logger = logger
        self.driver = driver

    def initialize_session(self):
        self.logger.info("Selenium driver call: get whatsapp web-page.")
        self.driver.get(WHATSAPP_WEBPAGE)

        self.logger.info("WhatsApp: session pending...")
        session_pending = True

        while session_pending:
            # Add delay time to reduce driver access frequency.
            time.sleep(SLEEP_TIME)

            try:
                qr_code = self.driver.find_element_by_tag_name("img")
                if WhatsAppConfig.QR_ALT_STRING not in qr_code.get_attribute("alt"):
                    self.logger.info("WhatsApp: session initialized.")
                    time.sleep(INITIAL_SLEEP_TIME)
                    session_pending = False

            except Exception:  # TODO: specify exceptions.
                self.logger.info("WhatsApp: Error: Assuming session initialized.")
                session_pending = False
                time.sleep(INITIAL_SLEEP_TIME) 

    def open_chat(self, user_name):
        self.logger.info("WhatsApp: method call open_chat for user %s" % user_name)
        self.driver.find_element_by_xpath(WhatsAppConfig.XPATH.CHAT_NEW).click()
        self.driver.find_element_by_id(WhatsAppConfig.ElementID.CHAT_LIST).send_keys(user_name)
        time.sleep(SLEEP_TIME)
        self.driver.find_element_by_xpath(WhatsAppConfig.XPATH.CHAT_AVATAR % user_name).click()
        time.sleep(SLEEP_TIME)

    def _find_text_box(self, divs):
        text_box = None
        for div in divs[::-1]:
            if "selectable-text" in div.get_attribute("class"):
                text_box = div
                break
        return text_box

    def send_message_text(self, content):
        self.logger.info("WhatsApp: method call send_message_text with content: %s" % content)
        divs = self.driver.find_elements_by_tag_name("div")
        text_box = self._find_text_box(divs)
        text_box.send_keys(content)
        self.driver.find_element_by_xpath(WhatsAppConfig.XPATH.BUTTON_TEXT_SEND).click()
        time.sleep(SLEEP_TIME)

    def send_message_media(self, media_path, caption=""):
        self.logger.info("WhatsApp: method call send_message_media with media_path %s and caption %s",
                         media_path, caption)

        self.driver.find_element_by_xpath(WhatsAppConfig.XPATH.BUTTON_ATTACH).click()
        self.driver.find_element_by_xpath(WhatsAppConfig.XPATH.BUTTON_FILE_INPUT).send_keys(media_path)
        time.sleep(SLEEP_TIME)

        if caption:
            divs = self.driver.find_elements_by_tag_name("div")
            text_box = self._find_text_box(divs[::-1])
            text_box.send_keys(caption)
            time.sleep(SLEEP_TIME)

        self.driver.find_element_by_xpath(WhatsAppConfig.XPATH.BUTTON_MEDIA_SEND).click()
        time.sleep(SLEEP_TIME)

    def close(self):
        self.driver.close()
