from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))

WebDriverWait(driver, 40).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

third_image_src = images[2].get_attribute("src")

print(third_image_src)

driver.quit()
