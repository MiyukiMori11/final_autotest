from .locators import BasketLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_empty_basket_message()
        self.should_not_be_any_items()

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET), \
            "There is no message that the trash is empty"

    def should_not_be_any_items(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_LIST), \
            "Basket is not empty"
