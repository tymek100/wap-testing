from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            raise TimeoutException(f"Element {by_locator} not visible after {timeout} seconds.")

    def click_element(self, by_locator):
        self.wait_for_element(by_locator)
        element = self.driver.find_element(*by_locator)
        element.click()

    def enter_text_with_enter(self, by_locator, text):
        self.wait_for_element(by_locator)
        element = self.driver.find_element(*by_locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def scroll_down(self, times=1, scroll_amount=None):
        for _ in range(times):
            amount = scroll_amount if scroll_amount else "window.innerHeight"
            self.driver.execute_script(f"window.scrollBy(0, {amount});")
            time.sleep(2)

    def take_screenshot(self, file_name):
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        path = os.path.join(screenshots_dir, file_name)
        self.driver.save_screenshot(path)
        print(f"Screenshot saved to {path}")

    def handle_popup_if_present(self, by_locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            self.driver.find_element(*by_locator).click()
        except TimeoutException:
            pass

    def is_element_in_viewport(self, element):
        is_in_viewport = self.driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect();"
            "return (rect.top >= 0 && rect.left >= 0 && rect.bottom <= window.innerHeight && rect.right <= window.innerWidth);",
            element
        )

        return is_in_viewport
