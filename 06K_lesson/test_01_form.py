from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_data_types_form():
    driver = webdriver.Edge()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java"
                   "/data-types.html")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form")))

        driver.find_element(
            By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
        driver.find_element(
            By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
        driver.find_element(
            By.CSS_SELECTOR, "input[name=address]").send_keys("Ленина, 55-3")

        driver.find_element(
            By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")

        driver.find_element(
            By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
        driver.find_element(
            By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
        driver.find_element(
            By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")

        driver.find_element(
            By.CSS_SELECTOR, "input[name=job-position]").send_keys("QA")
        driver.find_element(
            By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

        driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.ID, "zip-code"), "class", "alert-danger"))

        zip_code = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code.get_attribute(
            "class"), "Поле Zip code должно быть красным!"

        green_fields_ids = [
                "first-name", "last-name", "address", "e-mail",
                "phone", "city", "country", "job-position", "company"
            ]

        for field_id in green_fields_ids:
            field_element = driver.find_element(By.ID, field_id)
            assert "alert-success" in field_element.get_attribute(
                     "class"), f"Поле {field_id} должно быть зеленым!"
    finally:
        driver.quit()
