import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def get_product_info(self):
        product_name = self.get_element_text(ProductPageLocators.PRODUCT_TITLE)
        product_price = self.get_element_text(ProductPageLocators.PRICE)
        return product_name, product_price

    def check_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), '"Add to basket" button not found'
        assert self.is_element_present(*ProductPageLocators.ADD_TO_WISH_LIST_BTN), '"Add to wish list" button not found'
        assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW_LNK), '"Write a review" button not found'
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), 'Basket counter not found'

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_add_to_basket_message(self, name):
        assert self.is_element_present(ProductPageLocators.ADD_TO_BASKET_MSG[0],
                                       ProductPageLocators.ADD_TO_BASKET_MSG[1].format(name)), \
            'Added to basket message is not displayed'

    def get_element_text(self, locator):
        return self.browser.find_element(*locator).text

    def check_basket_total(self, price):
        current_price = self.get_element_text(ProductPageLocators.BASKET_TOTAL)
        assert current_price.startswith(f'Basket total: {price}'), f'{current_price} != {price}. Should be the same'

    def check_basket_notification(self, price):
        assert self.is_element_present(*ProductPageLocators.VIEW_BASKET_BTN), '"View basket" button not found'
        assert self.is_element_present(*ProductPageLocators.CHECKOUT_NOW_BTN), '"Checkout now" button not found'
        assert self.is_element_present(ProductPageLocators.BASKET_MSG[0],
                                       ProductPageLocators.BASKET_MSG[1].format(price)), \
            'Basket status message is wrong'

