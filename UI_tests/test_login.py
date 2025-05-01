import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from webdriver_manager import WebdriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep
# test for unseccussful login 4-5
# after login if it goes to Dashboard, element with My items text should be visible

@pytest.fixture
def driver():
    manager = WebdriverManager()
    manager.maximize_window()
    driver = manager.get_webdriver("http://alpha-player.bahrom04.uz/")
    yield driver
    manager.close_webdriver()


@pytest.mark.parametrize(
    "username, password", [
    ("myuser", "somepass123"),
    ("anotheruser1", "somepassway123"),
    ("cooluser", "strongpass"),])
def test_login_successful(driver, username, password):
    home_page = HomePage(driver)

    login_button = home_page.get_login_button()
    login_button.click()

    login_page = LoginPage(driver)

    username_field = login_page.get_username_field()
    password_field = login_page.get_password_field()
    submit_button = login_page.get_submit_button()

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

    WebDriverWait(driver, 4).until(EC.title_is("Welcome | Alpha player"))

    assert driver.title == "Welcome | Alpha player"

