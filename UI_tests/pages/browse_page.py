from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowsePage:
    driver: Chrome

    def __init__(self, driver):
        self.driver = driver

    def get_search_field(self):
        search_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Search what you want...']")
            )
        )

        return search_field
