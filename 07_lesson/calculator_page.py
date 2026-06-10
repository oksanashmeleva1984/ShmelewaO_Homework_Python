from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/"\
            "selenium-webdriver-java/slow-calculator.html"

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.spinner = (By.CSS_SELECTOR, "#spinner")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_input)
        )
        delay_element.clear()
        delay_element.send_keys(str(seconds))

    def click_button(self, text):
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        button_element.click()

    def get_result(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self.spinner)
        )

        return self.driver.find_element(*self.result_screen).text
