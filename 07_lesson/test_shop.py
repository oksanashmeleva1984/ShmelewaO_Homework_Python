import pytest
from selenium import webdriver
from shop_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


def test_saucedemo_shop(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item in items_to_add:
        inventory_page.add_to_cart(item)

    inventory_page.go_to_cart()

    items_in_cart = cart_page.get_item_names()
    for item in items_to_add:
        assert item in items_in_cart, f"Товара '{item}' нет в корзине!"

    cart_page.click_checkout()

    checkout_page.fill_checkout_form("Оксана", "Шмелева", "446100")

    total_price_text = checkout_page.get_total_price()

    expected_total = "$58.29"
    assert expected_total in total_price_text, (
        f"Ожидалась сумма {expected_total},"
        f" но на странице отображается: '{total_price_text}'"
    )
