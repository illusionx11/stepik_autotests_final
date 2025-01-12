from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
        
    def should_be_basket_page(self):
        self.should_have_basket_heading()
        
    def should_have_basket_heading(self):
        heading = self.browser.find_elements(*BasketPageLocators.BASKET_HEADING)
        assert len(heading) > 0, f"Basket heading element not found on requested page - {self.browser.current_url}"
        
    def should_have_empty_content(self):
        content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        content_text = content.text
        assert "Your basket is empty" in content_text, f"Expected 'Your basket is empty' text, got {content_text} - {self.browser.current_url}"
        
    def should_not_be_filled(self):
        assert self.is_element_not_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items element is present, but should not be"