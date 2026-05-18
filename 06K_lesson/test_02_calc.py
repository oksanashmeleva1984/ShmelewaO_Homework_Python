from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

        timeInput = driver.find_element(By.CSS_SELECTOR, "#delay")
        timeInput.clear()
        timeInput.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        wait = WebDriverWait(driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))
        result_text = driver.find_element(
            By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", (
             f"Ожидался результат 15, на экране отобразилось: {result_text}"
        )
    finally:

        driver.quit()
