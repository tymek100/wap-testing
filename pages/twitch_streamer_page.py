from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TwitchStreamerPage(BasePage):
    POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, '[data-a-target="content-classification-gate-overlay-start-watching-button"]')
    PLAYER_VIDEO = (By.CSS_SELECTOR, 'video')

    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        self.handle_popup_if_present(self.POPUP_CLOSE_BUTTON)

    def wait_for_stream_to_load(self):
        self.wait_for_element(self.PLAYER_VIDEO)
