import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MainPage,
    LoginPage,
    RegistrationPage,
    ForgotPasswordPage,
    BASE_URL,
)
from data_generators import generate_unique_email, generate_password


class TestLogin:
    """Тесты входа в систему разными способами"""

    def register_new_user(self, driver, user_data):
        """
        Вспомогательный метод: регистрирует нового пользователя через UI.
        Используется во всех тестах логина, где нужно заранее создать аккаунт.
        """
        driver.get(BASE_URL)

        # Переход на страницу регистрации
        login_button_main = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
        )
        login_button_main.click()

        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPage.REGISTER_LINK)
        )
        register_link.click()

        # Заполнение формы регистрации
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPage.NAME_INPUT)
        )
        name_input.send_keys(user_data["name"])

        email_input = driver.find_element(*RegistrationPage.EMAIL_INPUT)
        email_input.send_keys(user_data["email"])

        password_input = driver.find_element(*RegistrationPage.PASSWORD_INPUT)
        password_input.send_keys(user_data["password"])

        register_button = driver.find_element(*RegistrationPage.REGISTER_BUTTON)
        register_button.click()

        # Ждём заголовок "Вход"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.LOGIN_TITLE)
        )

    # 1) Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page_button(self, driver):
        """
        Вход по кнопке 'Войти в аккаунт' на главной странице.
        """
        # Регистрируем нового пользователя
        user_data = {
            "name": "Тестовый Пользователь",
            "email": generate_unique_email(),
            "password": generate_password(),
        }
        self.register_new_user(driver, user_data)

        # Открываем главную
        driver.get(BASE_URL)

        # Нажимаем кнопку "Войти в аккаунт"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
        )
        login_button.click()

        # Вводим данные для входа
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
        )
        email_input.send_keys(user_data["email"])

        password_input = driver.find_element(*LoginPage.PASSWORD_INPUT)
        password_input.send_keys(user_data["password"])

        # Нажимаем кнопку "Войти"
        login_submit_button = driver.find_element(*LoginPage.LOGIN_BUTTON)
        login_submit_button.click()

        # Проверяем, что вход выполнен
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        assert personal_account_button.is_displayed(), "Кнопка 'Личный кабинет' должна быть видна после входа"

    # 2) Вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver):
        """
        Вход через кнопку 'Личный кабинет' в шапке.
        """
        # Регистрируем нового пользователя
        user_data = {
            "name": "Тестовый Пользователь",
            "email": generate_unique_email(),
            "password": generate_password(),
        }
        self.register_new_user(driver, user_data)

        # Открываем главную
        driver.get(BASE_URL)

        # Нажимаем кнопку "Личный кабинет"
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Вводим данные для входа
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
        )
        email_input.send_keys(user_data["email"])

        password_input = driver.find_element(*LoginPage.PASSWORD_INPUT)
        password_input.send_keys(user_data["password"])

        # Нажимаем кнопку "Войти"
        login_button = driver.find_element(*LoginPage.LOGIN_BUTTON)
        login_button.click()

        # Проверяем успешный вход
        personal_account_button_after = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        assert personal_account_button_after.is_displayed(), "Кнопка 'Личный кабинет' должна быть видна после входа"

    # 3) Вход через ссылку в форме регистрации
    def test_login_from_registration_form(self, driver):
        """
        Вход через ссылку 'Войти' в форме регистрации.
        """
        # Регистрируем пользователя
        user_data = {
            "name": "Тестовый Пользователь",
            "email": generate_unique_email(),
            "password": generate_password(),
        }
        self.register_new_user(driver, user_data)

        # Переходим на страницу регистрации снова
        driver.get(BASE_URL)
        login_button_main = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
        )
        login_button_main.click()

        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPage.REGISTER_LINK)
        )
        register_link.click()

        # Нажимаем ссылку "Войти" под формой регистрации
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPage.LOGIN_LINK)
        )
        login_link.click()

        # Вводим данные для входа
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
        )
        email_input.send_keys(user_data["email"])

        password_input = driver.find_element(*LoginPage.PASSWORD_INPUT)
        password_input.send_keys(user_data["password"])

        # Нажимаем кнопку "Войти"
        login_button = driver.find_element(*LoginPage.LOGIN_BUTTON)
        login_button.click()

        # Проверяем успешный вход
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        assert personal_account_button.is_displayed(), "Кнопка 'Личный кабинет' должна быть видна после входа"

    # 4) Вход через ссылку в форме восстановления пароля
    def test_login_from_forgot_password_form(self, driver):
        """
        Вход через ссылку 'Войти' в форме восстановления пароля.
        """
        # Регистрируем пользователя
        user_data = {
            "name": "Тестовый Пользователь",
            "email": generate_unique_email(),
            "password": generate_password(),
        }
        self.register_new_user(driver, user_data)

        # Переходим на страницу восстановления пароля
        driver.get(BASE_URL)
        login_button_main = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
        )
        login_button_main.click()

        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPage.FORGOT_PASSWORD_LINK)
        )
        forgot_password_link.click()

        # Нажимаем ссылку "Войти" на странице восстановления пароля
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPage.LOGIN_LINK)
        )
        login_link.click()

        # Вводим данные для входа
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
        )
        email_input.send_keys(user_data["email"])

        password_input = driver.find_element(*LoginPage.PASSWORD_INPUT)
        password_input.send_keys(user_data["password"])

        # Нажимаем кнопку "Войти"
        login_submit_button = driver.find_element(*LoginPage.LOGIN_BUTTON)
        login_submit_button.click()

        # Проверяем успешный вход
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        assert personal_account_button.is_displayed(), "Кнопка 'Личный кабинет' должна быть видна после входа"
