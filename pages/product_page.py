from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_added_to_cart(self):
        self.should_be_addtocart_button()
        self.should_be_successful_added()
        self.should_be_correct_name()
        self.should_be_correct_price()

    def should_be_clicked_addtocart_button(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADDTOCART_BUTTON)
        button.click()

    def should_be_successful_added(self):
        self.should_be_clicked_addtocart_button()
        self.solve_quiz_and_get_code()
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_INFO
        ), "The product was not added"

    def should_be_addtocart_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADDTOCART_BUTTON
        ), "Add to cart button is not presented"

    def should_be_correct_name(self):
        name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        info = self.browser.find_element(
            *ProductPageLocators.INFO_NAME).text
        assert name == info, "Another product was added"

    def should_be_correct_price(self):
        price = self.browser.find_element(
            *ProductPageLocators.PRICE).text
        info = self.browser.find_element(
            *ProductPageLocators.INFO_PRICE).text
        assert price == info, "Another product was displayed"

    def cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_INFO), \
            "Success info was presented"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_INFO), \
            "The success message didn't disappear"
