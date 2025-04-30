from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebdriverManager():
    web_driver = None

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-insecure-localhost")

        self.web_driver = webdriver.Chrome(options=chrome_options)

    def get_webdriver(self, url: str):            
        self.web_driver.get(url)
        return self.web_driver
    
    def maximize_window(self):
        self.web_driver.maximize_window()
    
    def close_webdriver(self):
        if self.web_driver:
            self.web_driver.quit()

