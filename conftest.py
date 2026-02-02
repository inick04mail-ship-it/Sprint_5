import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators import MainPage, LoginPage
from urls import BASE_URL


@pytest.fixture(scope="function")
def driver():
    """Фикстура WebDriver: открывает Chrome перед тестом и закрывает после."""
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    _driver = webdriver.Chrome(options=options)
    _driver.maximize_window()

    yield _driver

    _driver.quit()


@pytest.fixture(scope="function")
def login_existing_user(driver):
    """Логинится под существующим пользователем через UI."""
    driver.get(BASE_URL)

    login_button_main = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
    )
    login_button_main.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
    )
    email_input.send_keys(EXISTING_USER_EMAIL)

    password_input = driver.find_element(*LoginPage.PASSWORD_INPUT)
    password_input.send_keys(EXISTING_USER_PASSWORD)

    login_button = driver.find_element(*LoginPage.LOGIN_BUTTON)
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPage.CONSTRUCTOR_TITLE)
    )

    return driver
