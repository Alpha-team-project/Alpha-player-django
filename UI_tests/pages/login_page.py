from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    driver: Chrome

    def __init__(self, driver):
        self.driver = driver
    
    def get_username_field(self):
        username_field = WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.ID, "id_username")))

        return username_field
    
    def get_password_field(self):
        return self.driver.find_element(By.ID, "id_password")

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Submit']")

