import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPage, LoginPage, RegistrationPage, BASE_URL
from data_generators import generate_unique_email, generate_password


class TestRegistration:
    """Тесты регистрации пользователей"""

    def test_successful_registration(self, driver):
        """
        Успешная регистрация с валидными данными.
        Имя не пустое, email в формате логин@домен, пароль >= 6 символов.
        """
        user_data = {
            "name": "Тестовый Пользователь",
            "email": generate_unique_email(),
            "password": generate_password(min_length=6),
        }

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

        # Ожидаем переход на форму входа
        login_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.LOGIN_TITLE)
        )
        assert login_title.is_displayed(), "После успешной регистрации должна открыться форма входа"

    def test_registration_with_incorrect_password(self, driver):
        """
        Регистрация с некорректным (слишком коротким) паролем.
        Должно появиться сообщение об ошибке.
        """
        user_data = {
            "name": "Тестовый Пользователь",
            "email": generate_unique_email(),
            "password": "12345",  # меньше 6 символов
        }

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

        # Проверяем сообщение об ошибке пароля
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPage.ERROR_MESSAGE)
        )
        assert error_message.is_displayed(), "Должно появиться сообщение об ошибке для некорректного пароля"
