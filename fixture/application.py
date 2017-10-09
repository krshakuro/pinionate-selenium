from selenium.webdriver.chrome.webdriver import WebDriver

from pages.widget import Widget

__author__ = 'kirill'

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.widget = Widget(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://pinion.shakuro.net/")

    def destroy(self):
        self.wd.quit()