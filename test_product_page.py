import pytest
from .pages.product_page import ProductPage
import time

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