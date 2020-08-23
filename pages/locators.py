from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    ADDTOCART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_INFO = (By.CSS_SELECTOR, "div.alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    INFO_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    INFO_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
