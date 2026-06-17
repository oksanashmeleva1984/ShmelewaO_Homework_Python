from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
sleep(2)
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(2)
button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
button_login.click()
sleep(2)

flash_message = driver.find_element(By.ID, "flash").text
print(f"Текст с плашки: {flash_message}")
driver.quit()
