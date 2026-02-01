import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import DEFAULT_USER_NAME
from data_generators import generate_unique_email, generate_password
from helpers import (
    go_to_login_from_main,
    go_to_registration_from_main,
    go_to_forgot_password_from_main,
    fill_registration_form,
    wait_for_login_form,
    fill_login_form_and_submit,
    wait_for_authorized_main_page,
)
from locators import MainPage, LoginPage, RegistrationPage, ForgotPasswordPage


class TestLogin:
    """Тесты входа в систему разными способами"""

    def register_new_user(self, driver):
        """Регистрирует нового пользователя через UI и возвращает user_data."""
        user_data = {
            "name": DEFAULT_USER_NAME,
            "email": generate_unique_email(),
            "password": generate_password(),
        }

        go_to_registration_from_main(driver)
        fill_registration_form(driver, user_data)
        wait_for_login_form(driver)  # после регистрации попадаем на форму входа

        return user_data

    # 1) Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page_button(self, driver):
        """Вход по кнопке 'Войти в аккаунт' на главной странице."""
        user_data = self.register_new_user(driver)

        go_to_login_from_main(driver)
        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button = wait_for_authorized_main_page(driver)
        assert (
            personal_account_button.is_displayed()
        ), "Кнопка 'Личный кабинет' должна быть видна после входа"

    # 2) Вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет' в шапке."""
        user_data = self.register_new_user(driver)

        from urls import BASE_URL

        driver.get(BASE_URL)

        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button_after = wait_for_authorized_main_page(driver)
        assert (
            personal_account_button_after.is_displayed()
        ), "Кнопка 'Личный кабинет' должна быть видна после входа"

    # 3) Вход через ссылку в форме регистрации
    def test_login_from_registration_form(self, driver):
        """Вход через ссылку 'Войти' в форме регистрации."""
        user_data = self.register_new_user(driver)

        # Снова переходим на форму регистрации
        from urls import BASE_URL

        driver.get(BASE_URL)
        go_to_registration_from_main(driver)

        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPage.LOGIN_LINK)
        )
        login_link.click()

        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button = wait_for_authorized_main_page(driver)
        assert (
            personal_account_button.is_displayed()
        ), "Кнопка 'Личный кабинет' должна быть видна после входа"

    # 4) Вход через ссылку в форме восстановления пароля
    def test_login_from_forgot_password_form(self, driver):
        """Вход через ссылку 'Войти' в форме восстановления пароля."""
        user_data = self.register_new_user(driver)

        # Переходим на страницу восстановления пароля
        go_to_forgot_password_from_main(driver)

        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPage.LOGIN_LINK)
        )
        login_link.click()

        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button = wait_for_authorized_main_page(driver)
        assert (
            personal_account_button.is_displayed()
        ), "Кнопка 'Личный кабинет' должна быть видна после входа"
