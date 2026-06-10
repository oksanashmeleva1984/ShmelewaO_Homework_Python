from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.CSS_SELECTOR, "#user-name")
        self.password_input = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_to_cart(self, item_name):
        add_button_xpath = (
            f"//div[text()='{item_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, add_button_xpath)))
        self.driver.find_element(By.XPATH, add_button_xpath).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")
        self.cart_item_name = (By.CSS_SELECTOR, ".inventory_item_name")

    def get_item_names(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cart_item_name))
        elements = self.driver.find_elements(*self.cart_item_name)
        return [el.text for el in elements]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.CSS_SELECTOR, "#first-name")
        self.last_name_input = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_input = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.CSS_SELECTOR, "#continue")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_name_input))
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(
            postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label))
        return self.driver.find_element(*self.total_label).text
