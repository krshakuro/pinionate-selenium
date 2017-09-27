from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class Widget:

    def __init__(self, wd):
        self.wd = wd
        wd.wait = WebDriverWait(wd, 10)

    def open(self):
        self.wd.get("http://pinionate.com")
        self.wd.find_element_by_css_selector("channel-preview").click()
        self.wd.switch_to_frame(0)
        return self

    @property
    def like_by_button(self):
        return self.wd.find_element_by_css_selector(".pinion-like-btn").click()

    @property
    def dislike_by_button(self):
        return self.wd.find_element_by_css_selector(".pinion-dislike-btn").click()

    @property
    def skip_by_button(self):
        return self.wd.find_element_by_css_selector(".pinion-skip-btn").click()

    @property
    def like_by_swipe(self):

    @property
    def dislike_by_swipe(self):

    @property
    def skip_by_swipe(self):

    @property
    def maximize_by_button(self):

    @property
    def maximize_by_click(self):

    @property
    def review(self):

    @property
    def back(self):

    @property
    def close(self):



