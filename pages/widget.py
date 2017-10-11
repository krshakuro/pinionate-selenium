import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait


class Widget:

    def __init__(self, app):
        self.app = app

    def open_widget(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(".channel-preview__image").click()

    def close_channel_info(self):
        wd = self.app.wd
        close_channel_info_btn = WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".pinion-channel-info-toggle-btn"))
        )
        close_channel_info_btn.click()

    def init_widget(self):
        wd = self.app.wd
        wd.switch_to.frame(0)

    def close_widget(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-cancel-fullscreen-btn").click()

    # def like_by_btn(self):
    #     wd = self.app.wd
    #     # like_btn = wd.find_element_by_css_selector(".pinion-like-btn")
    #     # image = wd.find_element_by_css_selector(".pinion-crop-center")
    #     wait = WebDriverWait(wd, 30)
    #     wait.until(lambda  wd: wd.find_element(By.CLASS_NAME,"pinion-like-btn")
    #                            and wd.find_element(By.CLASS_NAME, "pinion-crop-center"))
    #     wd.find_element_by_css_selector(".pinion-like-btn").click()

     def like_by_btn(self):
        wd = self.app.wd
        # like_btn = wd.find_element_by_css_selector(".pinion-like-btn")
        # image = wd.find_element_by_css_selector(".pinion-crop-center")
        wait = WebDriverWait(wd, 30)
        wait.until(lambda  wd: wd.find_element(By.CLASS_NAME,"pinion-like-btn")
                               and wd.find_element(By.CLASS_NAME, "pinion-crop-center"))
        wd.find_element_by_css_selector(".pinion-like-btn").click()


    def dislike_by_btn(self):
        wd = self.app.wd
        dislike_btn = WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".pinion-dislike-btn")))
        dislike_btn.click()

    def skip_by_btn(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-skip-btn").click()

    def like_by_swipe(self):
        wd = self.app.wd
        action_chains = ActionChains(wd)
        action_chains.drag_and_drop(wd.find_element_by_css_selector(".pinion-crop-center"), wd.find_element_by_css_selector(".pinion-cancel-fullscreen-btn")).perform()

    def dislike_by_swipe(self):
        wd = self.app.wd
        action_chains = ActionChains(wd)
        action_chains.drag_and_drop(wd.find_element_by_css_selector(".pinion-crop-center"), wd.find_element_by_css_selector(".pinion-avatar")).perform()

    def skip_by_swipe(self):
        wd = self.app.wd
        action_chains = ActionChains(wd)
        action_chains.drag_and_drop(wd.find_element_by_css_selector(".pinion-crop-center"), wd.find_element_by_css_selector(".pinion-cont")).perform()

    def review_jumping(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-collection-item-question").click()

    def open_positive_review(self):
        wd = self.app.wd
        wd.find_element_by_link_text("My Positive").click()

    def open_negative_review(self):
        wd = self.app.wd
        wd.find_element_by_link_text("My Negative").click()

    def expand_by_btn(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-content").click()
        time.sleep(1)
        wd.find_element_by_css_selector(".pinion-content").click()

    def click_link_button(self):
        wd = self.app.wd
        wd.find_element_b

    def click_buy_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-external-buy").click()

    def click_info_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".pinion-description-toggle-btn").click()

    def negative_votes_count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector(".pinion-collection-item-vote-negative"))
