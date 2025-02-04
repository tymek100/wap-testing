from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class TwitchHomePage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, "a[href='/directory']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[data-a-target='tw-input']")
    COOKIES_ACCEPT_FIELD = (By.CSS_SELECTOR, "button[data-a-target='consent-banner-accept']")
    VIDEO_THUMBNAILS = (By.CSS_SELECTOR, "img.tw-image")

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, url="https://www.twitch.tv/"):
        self.driver.get(url)

    def click_search_icon(self):
        self.click_element(self.SEARCH_ICON)

    def search_for_game(self, game_name="StarCraft II"):
        self.enter_text_with_enter(self.SEARCH_FIELD, game_name)

    def close_cookies_popup(self):
        self.handle_popup_if_present(self.COOKIES_ACCEPT_FIELD)

    def wait_for_thumbnails_to_load(self):
        self.wait_for_element(self.VIDEO_THUMBNAILS)
        thumbnails = self.driver.find_elements(*self.VIDEO_THUMBNAILS)
        for img in thumbnails: # ensure each image has a valid 'src' attribute
            self.wait_for_element((By.XPATH, f"//img[@src='{img.get_attribute('src')}']"))

    def click_first_streamer(self):
        self.wait_for_element(self.VIDEO_THUMBNAILS)
        thumbnails = self.driver.find_elements(*self.VIDEO_THUMBNAILS)
        for thumbnail in thumbnails:
            if self.is_element_in_viewport(thumbnail):
                thumbnail.click()
                return
