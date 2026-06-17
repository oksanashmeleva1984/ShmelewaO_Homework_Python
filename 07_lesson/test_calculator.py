import pytest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_slow_calculator(driver):
    page = SlowCalculatorPage(driver)

    page.open()

    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result(timeout=50)

    assert result == "15", (
        f"Ожидался результат 15, но калькулятор показал: {result}"
    )
