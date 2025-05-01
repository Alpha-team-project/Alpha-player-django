from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    driver: Chrome

    def __init__(self, driver):
        self.driver = driver

    def get_search_bar_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='Browse']"))
        )

    def get_contact_button(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Contact']")

    def get_dashboard_button(self):
        return self.driver.find_element(By.XPATH, "//a[@href='/dashboard/']")

    def get_login_button(self):
        login_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']"))
        )

        return login_button
