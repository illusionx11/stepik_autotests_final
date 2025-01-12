from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    BASKET_LINK = (By.XPATH, "//a[text()='View basket']")
    
class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")
    
class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    WRITE_REVIEW_BTN = (By.ID, "write_review")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    ALERT_BOOK_PRICE = (By.CSS_SELECTOR, "#messages .alert:last-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner")
    
class BasketPageLocators():
    BASKET_HEADING = (By.CSS_SELECTOR, ".page-header h1")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")