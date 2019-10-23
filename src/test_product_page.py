import pytest
from .pages.product_page import ProductPage


# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    name, price = page.get_product_info()
    page.check_product_page()
    page.check_basket_total('£0.00')
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_add_to_basket_message(name)
    page.check_basket_total(price)
    page.check_basket_notification(price)


