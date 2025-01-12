from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    WRITE_REVIEW_BTN = (By.ID, "write_review")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    ALERT_BOOK_PRICE = (By.CSS_SELECTOR, "#messages .alert:last-child strong")