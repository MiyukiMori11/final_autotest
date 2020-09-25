from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url,\
            'Current page is not login page'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), 'Register form not found'

    def register_new_user(self, email, password):
        reg_data = (email, password, password)
        counter = 0
        form = self.browser.find_elements(*LoginPageLocators.REGISTER_FIELDS)
        for row in form:
            row.send_keys(reg_data[counter])
            counter += 1
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

