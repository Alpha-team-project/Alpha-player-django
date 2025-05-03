from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyplaylistPage():
    driver: Chrome

    def __init__(self, driver):
        self.driver = driver
    
    def get_myplaylist_element(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='My playlist']")))

