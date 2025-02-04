import pytest
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_streamer_page import TwitchStreamerPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
class TestWAPTwitch:

    def test_twitch_starcraft_stream(self, driver):
        home = TwitchHomePage(driver)

        home.open_home_page()
        home.close_cookies_popup()
        home.click_search_icon()
        home.search_for_game("StarCraft II")
        home.wait_for_thumbnails_to_load()
        home.scroll_down(times=2, scroll_amount=150)
        home.click_first_streamer()

        streamer_page = TwitchStreamerPage(driver)

        streamer_page.close_popup()
        streamer_page.wait_for_stream_to_load()
        streamer_page.take_screenshot("starcraft_streamer.png")
