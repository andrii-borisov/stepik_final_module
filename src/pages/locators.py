from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_TOTAL = (By.XPATH, "//div[strong[text()='Basket total:']]")
    WRITE_REVIEW_LNK = (By.ID, "write_review")
    ADD_TO_WISH_LIST_BTN = (By.XPATH, "//button[text()='Add to wish list']")
    ADD_TO_BASKET_BTN = (By.XPATH, "//button[text()='Add to basket']")
    VIEW_BASKET_BTN = (By.LINK_TEXT, 'View basket')
    CHECKOUT_NOW_BTN = (By.LINK_TEXT, 'Checkout now')
    PRODUCT_TITLE = (By.XPATH, '//h1')
    PRICE = (By.XPATH, '//p[@class="price_color"]')
    ADD_TO_BASKET_MSG = (By.XPATH, '//div[strong[text()="{0}"] and normalize-space(text()="has been added to your basket.")]')
    BASKET_MSG = (By.XPATH, '//p[normalize-space(text()="Your basket total is now") and strong[text()="{0}"]]')

