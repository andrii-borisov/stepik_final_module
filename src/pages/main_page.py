from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        link_ = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link_.click()




