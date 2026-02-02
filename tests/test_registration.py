from data import DEFAULT_USER_NAME, VALID_PASSWORD_MIN_LENGTH
from data_generators import generate_unique_email
from helpers import (
    go_to_registration_from_main,
    fill_registration_form,
    wait_for_login_form,
    get_registration_error_message,
)


class TestRegistration:
    """Тесты регистрации пользователей."""

    def test_successful_registration(self, driver):
        """Успешная регистрация с валидными данными."""
        user_data = {
            "name": DEFAULT_USER_NAME,
            "email": generate_unique_email(),
            "password": "A" * VALID_PASSWORD_MIN_LENGTH,
        }

        go_to_registration_from_main(driver)
        fill_registration_form(driver, user_data)

        login_title = wait_for_login_form(driver)
        assert login_title.is_displayed(), (
            "После успешной регистрации должна открыться форма входа"
        )

    def test_registration_with_incorrect_password(self, driver):
        """Регистрация с некорректным (слишком коротким) паролем."""
        user_data = {
            "name": DEFAULT_USER_NAME,
            "email": generate_unique_email(),
            "password": "12345",
        }

        go_to_registration_from_main(driver)
        fill_registration_form(driver, user_data)

        error_message = get_registration_error_message(driver)
        assert error_message.is_displayed(), (
            "Должно появиться сообщение об ошибке для некорректного пароля"
        )
