from selenium import webdriver
from pages.widget import Widget

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.widget = Widget(self.wd)

    def quit(self):
        self.wd.quit()