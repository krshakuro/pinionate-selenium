from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class Widget:

    def __init__(self, app):
        self.app = app

    def open_widget(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(".channel-preview__image").click()

    def close_channel_info(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-channel-info-toggle-btn").click()

    def init_widget(self):
        wd = self.app.wd
        wd.switch_to.frame(0)

    def close_widget(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-cancel-fullscreen-btn").click()

    def like_by_btn(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-like-btn").click()

    def dislike_by_btn(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-dislike-btn").click()

    def dislike_by_btn(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-dislike-btn").click()


