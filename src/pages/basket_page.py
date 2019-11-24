from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()
        self.should_be_basket_breadcrumb()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, 'URI is wrong'

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), 'There is no basket header'

    def should_be_basket_breadcrumb(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BREADCRUMB), 'There is no basket breadcrumb'

    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_CONTENT), 'Basket is not empty'

    def basket_does_not_contains_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), 'Basket is not empty'

    def check_shopping_link_in_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), 'There is no Continue shopping link'
