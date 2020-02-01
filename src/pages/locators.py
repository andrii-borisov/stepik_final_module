from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.LINK_TEXT, "View basket")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOG_IN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOG_IN_BTN = (By.XPATH, "//button[text()='Log In']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.XPATH, "//button[text()='Register']")


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


class BasketPageLocators:
    BASKET_HEADER = (By.XPATH, "//h1")
    BASKET_BREADCRUMB = (By.XPATH, "//ul[@class='breadcrumb']/li[@class='active' and text()='Basket']")
    EMPTY_BASKET_CONTENT = (By.XPATH, "//div[@id='content_inner']/p[contains(text(),'Your basket is empty.')]")
    CONTINUE_SHOPPING_LINK = (By.LINK_TEXT, "Continue shopping")
    BASKET_ITEM = (By.XPATH, "//div[@class='basket-items']")



