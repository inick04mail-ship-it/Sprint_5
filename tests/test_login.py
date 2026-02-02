from helpers import (
    go_to_login_from_main,
    go_to_registration_from_main,
    go_to_forgot_password_from_main,
    fill_registration_form,
    wait_for_login_form,
    fill_login_form_and_submit,
    wait_for_authorized_main_page,
    register_new_user,
    click_element,
)
from locators import MainPage, RegistrationPage, ForgotPasswordPage
from urls import BASE_URL


class TestLogin:
    """Тесты входа в систему разными способами."""

    def test_login_from_main_page_button(self, driver):
        """Вход по кнопке 'Войти в аккаунт' на главной странице."""
        user_data = register_new_user(driver)

        go_to_login_from_main(driver)
        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button = wait_for_authorized_main_page(driver)
        assert personal_account_button.is_displayed(), (
            "Кнопка 'Личный кабинет' должна быть видна после входа"
        )

    def test_login_from_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет' в шапке."""
        user_data = register_new_user(driver)

        driver.get(BASE_URL)
        click_element(driver, MainPage.PERSONAL_ACCOUNT_BUTTON)

        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button_after = wait_for_authorized_main_page(driver)
        assert personal_account_button_after.is_displayed(), (
            "Кнопка 'Личный кабинет' должна быть видна после входа"
        )

    def test_login_from_registration_form(self, driver):
        """Вход через ссылку 'Войти' в форме регистрации."""
        user_data = register_new_user(driver)

        driver.get(BASE_URL)
        go_to_registration_from_main(driver)

        click_element(driver, RegistrationPage.LOGIN_LINK)

        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button = wait_for_authorized_main_page(driver)
        assert personal_account_button.is_displayed(), (
            "Кнопка 'Личный кабинет' должна быть видна после входа"
        )

    def test_login_from_forgot_password_form(self, driver):
        """Вход через ссылку 'Войти' в форме восстановления пароля."""
        user_data = register_new_user(driver)

        go_to_forgot_password_from_main(driver)

        click_element(driver, ForgotPasswordPage.LOGIN_LINK)

        fill_login_form_and_submit(driver, user_data["email"], user_data["password"])

        personal_account_button = wait_for_authorized_main_page(driver)
        assert personal_account_button.is_displayed(), (
            "Кнопка 'Личный кабинет' должна быть видна после входа"
        )
