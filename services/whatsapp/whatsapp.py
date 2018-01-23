import time

WHATSAPP_WEBPAGE = "https://web.whatsapp.com/"
SLEEP_TIME = 3


class WhatsApp(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(WHATSAPP_WEBPAGE)
        self.initialize_session()

    def initialize_session(self):
        session_pending = True
        while session_pending:
            time.sleep(SLEEP_TIME)
            try:
                qr_code = self.driver.find_element_by_tag_name("img")
                if "Scan me!" not in qr_code.get_attribute("alt"):
                    session_pending = False
            except Exception:  # TODO: specify exceptions.
                session_pending = False

    def open_chat(self, user_name):
        self.driver.find_element_by_xpath("//div[@title='New chat']").click()
        self.driver.find_element_by_id("input-chatlist-search").send_keys(user_name)
        time.sleep(SLEEP_TIME)
        self.driver.find_element_by_xpath("//div[@class='chat-avatar']").click()

    def send_message_text(self, content):
        self.driver.find_element_by_xpath("//div[@class='pluggable-input-body copyable-text selectable-text']") \
            .send_keys(content)
        self.driver.find_element_by_xpath("//button[@class='compose-btn-send']").click()

    def send_message_media(self, media_path, caption=""):
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

