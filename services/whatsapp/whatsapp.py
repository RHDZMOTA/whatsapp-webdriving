import time

from settings import SLEEP_TIME, WHATSAPP_WEBPAGE


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
                if "Scan me!" not in qr_code.get_attribute("alt"):
                    self.logger.info("WhatsApp: session initialized.")
                    session_pending = False

            except Exception:  # TODO: specify exceptions.
                self.logger.info("WhatsApp: Error: Assuming session initialized.")
                session_pending = False

    def open_chat(self, user_name):
        self.logger.info("WhatsApp: method call open_chat for user %s" % user_name)
        self.driver.find_element_by_xpath("//div[@title='New chat']").click()
        self.driver.find_element_by_id("input-chatlist-search").send_keys(user_name)
        time.sleep(SLEEP_TIME)
        self.driver.find_element_by_xpath("//div[@class='chat-avatar']").click()

    def send_message_text(self, content):
        self.logger.info("WhatsApp: method call send_message_text with content: %s" % content)
        self.driver.find_element_by_xpath("//div[@class='pluggable-input-body copyable-text selectable-text']") \
            .send_keys(content)
        self.driver.find_element_by_xpath("//button[@class='compose-btn-send']").click()

    def send_message_media(self, media_path, caption=""):
        self.logger.info("WhatsApp: method call send_message_media with media_path %s and caption %s" % (media_path, caption))

        self.driver.find_element_by_xpath("//div[@title='Attach']").click()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(media_path)
        time.sleep(SLEEP_TIME)

        if caption:
            self.driver.find_element_by_xpath("//div[@class='pluggable-input-body copyable-text selectable-text']") \
                .send_keys(caption)
            time.sleep(SLEEP_TIME)

        self.driver.find_element_by_xpath("//span[@data-icon='send-light']").click()

    def close(self):
        self.driver.close()

