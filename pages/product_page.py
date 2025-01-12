from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_button()
        self.should_be_write_review_button()
        
    def should_be_product_url(self):
        current_url = self.browser.current_url
        assert "catalogue" in current_url, f"Current URL doesn't have 'catalogue' substring - {current_url}"
        
    def should_be_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_elements(*ProductPageLocators.ADD_TO_BASKET_BTN)
        assert len(add_to_basket_button) > 0, f"Add to Basket Button is not present on current page - {self.browser.current_url}"
        
    def should_be_write_review_button(self):
        write_review_button = self.browser.find_elements(*ProductPageLocators.WRITE_REVIEW_BTN)
        assert len(write_review_button) > 0, f"Write Review Button is not present on current page - {self.browser.current_url}"
        
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        
    def add_to_basket_should_pop_up_alert(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        assert alert_text.split(" ")[0] == "x", f"Wrong alert popped up on page {self.browser.current_url}"

    def product_should_be_added_to_basket(self):    
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        
        book_title_alert = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME).text
        book_price_alert = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_PRICE).text
        
        assert book_title == book_title_alert, f"Book title is not the same. Expected '{book_title}', got '{book_title_alert}'"
        assert book_price == book_price_alert, f"Book price is not the same. Expected '{book_price}', got '{book_price_alert}'"
        
    def should_not_be_success_message(self):
        assert self.is_element_not_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
            
    def should_element_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but it should"
    
    