from .pages.product_page import ProductPage
import pytest


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
