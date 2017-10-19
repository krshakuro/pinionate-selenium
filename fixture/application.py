from selenium.webdriver.chrome.webdriver import WebDriver

from pages.widget import Widget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__author__ = 'kirill'

class Application:

    def __init__(self):

        self.widget = Widget(self)
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.wd = webdriver.Chrome(chrome_options=chrome_options)
        self.wd.implicitly_wait(5)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://pinion.shakuro.net/")

    def open_link_page(self):
        wd = self.wd
        wd.get("http://pinionate.com/channel/440/Best-Dog-Breeds")

    def open_buy_page(self):
        wd = self.wd
        wd.get("http://pinion.shakuro.net/channel/478/Teen-Girl-Halloween-Costume-Ideas")

    def open_info_page(self):
        wd = self.wd
        wd.get("http://pinion.shakuro.net/channel/356/Environmental-Policies-Since-Trump")

    def refresh(self):
        wd = self.wd
        wd.refresh()

    def first_avatar_opening(self):
        wd = self.wd
        wd.find_element_by_css_selector(".channel-preview__user-avatar").click()

    def destroy(self):
        self.wd.quit()