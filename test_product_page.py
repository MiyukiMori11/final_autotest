from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import random


@pytest.mark.addtobasket_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = f'{random.randint(0000000, 999999)}@pochta.ru'
        password = 'abcdefg123456'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                      pytest.param(7, marks=pytest.mark.xfail),
                                      8, 9])
    def test_user_can_add_product_to_basket(self, browser, link):
        link = f'http://selenium1py.pythonanywhere.com/catalogue' \
               f'/coders-at-work_207/?promo=offer{link} '
        page = ProductPage(browser, link)
        page.open()
        page.should_be_added_to_cart()

    def test_user_cant_see_success_message(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue' \
               f'/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.cant_see_success_message()


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue' \
           f'/coders-at-work_207/?promo=offer{link} '
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_cart()


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue' \
           f'/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_clicked_addtocart_button()
    page.cant_see_success_message()


def test_guest_cant_see_success_message(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue' \
           f'/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.cant_see_success_message()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue' \
           f'/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_clicked_addtocart_button()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
