import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from helpers import login_with_existing_user


@pytest.fixture(scope="function")
def driver():
    """Фикстура WebDriver: открывает Chrome перед тестом и закрывает после."""
    options = Options()
    options.add_argument("--window-size=1920,1080")

    _driver = webdriver.Chrome(options=options)
    _driver.maximize_window()

    yield _driver

    _driver.quit()


@pytest.fixture(scope="function")
def login_existing_user(driver):
    """Логинится под существующим пользователем через UI."""
    login_with_existing_user(driver, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD)
    return driver
