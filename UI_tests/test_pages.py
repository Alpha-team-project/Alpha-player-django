import pytest
from pages.home_page import HomePage
from pages.browse_page import BrowsePage
from pages.login_page import LoginPage
from pages.myplaylist_page import MyplaylistPage
from webdriver_manager import WebdriverManager


@pytest.fixture
def driver():
    manager = WebdriverManager()
    manager.maximize_window()
    driver = manager.get_webdriver("http://alpha-player.bahrom04.uz/")
    yield driver
    manager.close_webdriver()


def test_browse_page_title(driver):
    home_page = HomePage(driver)

    browse_button = home_page.get_search_bar_button()
    browse_button.click()

    assert driver.title == "Items | Alpha player"


def test_contact_page_title(driver):
    home_page = HomePage(driver)

    contact_button = home_page.get_contact_button()
    contact_button.click()

    assert driver.title == "Contact | Alpha player"


def test_dashboard_page_title(driver):
    home_page = HomePage(driver)

    login_button = home_page.get_login_button()
    login_button.click()

    login_page = LoginPage(driver)
    username_field = login_page.get_username_field()
    password_field = login_page.get_password_field()
    submit_button = login_page.get_submit_button()

    username_field.send_keys("myuser")
    password_field.send_keys("somepass123")
    submit_button.click()

    dashboard_button = home_page.get_dashboard_button()
    dashboard_button.click()

    assert driver.title == "Dashboard | Alpha player"


def test_browse_page_search_field(driver):
    home_page = HomePage(driver)

    browse_button = home_page.get_search_bar_button()
    browse_button.click()

    browse_page = BrowsePage(driver)
    search_field = browse_page.get_search_field()

    assert search_field.is_displayed() is True

def test_myplaylist_page(driver):
    home_page = HomePage(driver)

    login_button = home_page.get_login_button()
    login_button.click()

    login_page = LoginPage(driver)

    username_field = login_page.get_username_field()
    password_field = login_page.get_password_field()
    submit_button = login_page.get_submit_button()

    username_field.send_keys("myuser")
    password_field.send_keys("somepass123")
    submit_button.click()

    myplaylist_button = home_page.get_myplaylist_button()
    myplaylist_button.click()

    playlist_page = MyplaylistPage(driver)

    myplaylist_element = playlist_page.get_myplaylist_element()

    assert myplaylist_element.is_displayed() is True

