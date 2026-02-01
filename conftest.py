import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPage, LoginPage, BASE_URL


# Мой аккаунт
TEST_USER_EMAIL = "Nickolay_Inkh_39990@yandex.ru"
TEST_USER_PASSWORD = "Nickolay_Inkh_39990"


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL приложения."""
    return BASE_URL


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура WebDriver.
    Открывает Chrome перед тестом и закрывает после.
    """
    options = Options()
    # options.add_argument("--headless")  # можно включить, если не нужен видимый браузер
    options.add_argument("--window-size=1920,1080")

    _driver = webdriver.Chrome(options=options)
    _driver.maximize_window()

    yield _driver

    _driver.quit()


@pytest.fixture(scope="function")
def login_existing_user(driver, base_url):
   
    driver.get(base_url)

    # Нажимаем "Войти в аккаунт"
    login_button_main = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
    )
    login_button_main.click()

    # Вводим логин и пароль
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
    )
    email_input.send_keys(TEST_USER_EMAIL)

    password_input = driver.find_element(*LoginPage.PASSWORD_INPUT)
    password_input.send_keys(TEST_USER_PASSWORD)

    # Нажимаем "Войти"
    login_button = driver.find_element(*LoginPage.LOGIN_BUTTON)
    login_button.click()

   
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPage.CONSTRUCTOR_TITLE)
    )

    return driver
