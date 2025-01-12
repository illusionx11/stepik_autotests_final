import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

DEFAULT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

links = []
for i in range(10):
    if i != 7:
        links.append(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}")
    else:
        links.append(pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}", marks=pytest.mark.xfail))

@pytest.mark.parametrize("link", links)
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

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_filled()
    basket_page.should_have_empty_content()
    
