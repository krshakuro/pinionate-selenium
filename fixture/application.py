from selenium.webdriver.chrome.webdriver import WebDriver

from pages.widget import Widget

__author__ = 'kirill'

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.widget = Widget(self)

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
        wd.get("http://pinion.shakuro.net/")

    def open_buy_page(self):
        wd = self.wd
        wd.get("http://pinion.shakuro.net/")

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