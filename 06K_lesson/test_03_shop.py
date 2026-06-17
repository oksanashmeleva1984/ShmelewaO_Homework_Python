from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.ID, "user-name")))

        driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()

        wait.until(EC.presence_of_element_located(
            (By.ID, "inventory_container")))

        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()

        wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        wait.until(
            EC.presence_of_element_located((By.ID, "first-name")))
        driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Оксана")
        driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Шмелева")
        driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("446100")
        driver.find_element(
            By.CSS_SELECTOR, "#continue").click()

        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        total_text = driver.find_element(
            By.CLASS_NAME, "summary_total_label").text

        assert total_text == "Total: $58.29", (
             f"Ожидался результат 'Total:$58.29', получилось: {total_text} "
        )

    finally:
        driver.quit()
