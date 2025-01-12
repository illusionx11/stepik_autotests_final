import pytest
from .pages.product_page import ProductPage
import time

DEFAULT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

links = []
for i in range(10):
    if i != 7:
        links.append(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}")
    else:
        links.append(pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}", marks=pytest.mark.xfail))

@pytest.mark.parametrize("link", links)
@pytest.mark.skip()
def test_guest_can_add_product_to_basket(browser, link):
    
    print(f"link: {link}")
    page = ProductPage(browser, link)
    browser.delete_all_cookies()
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.add_to_basket_should_pop_up_alert()
    page.solve_quiz_and_get_code()
    page.product_should_be_added_to_basket()
    
@pytest.mark.xfail(reason="Bad test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, DEFAULT_LINK, 0)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, DEFAULT_LINK, 0)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Bad test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, DEFAULT_LINK, 0)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_element_disappear()
