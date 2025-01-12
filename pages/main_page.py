from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):
    
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Should be a login link but there is not"