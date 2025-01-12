from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"Current URL doesn't have 'login' substring - {current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert len(login_form) > 0, f"Login form is not present on current page - {self.browser.current_url}"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        reg_form = self.browser.find_elements(*LoginPageLocators.REG_FORM)
        assert len(reg_form) > 0, f"Registration form is not present on current page - {self.browser.current_url}"