from helpers import (
    go_to_personal_account,
    click_element,
    get_element_text,
)
from locators import MainPage, PersonalAccountPage, LoginPage


class TestNavigation:
    """Тесты навигации для уже авторизованного пользователя."""

    def test_navigate_to_personal_account(self, driver, login_existing_user):
        """Переход в личный кабинет при нажатии на 'Личный кабинет'."""
        go_to_personal_account(driver)

        profile_title_text = get_element_text(
            driver, PersonalAccountPage.PROFILE_TITLE
        )
        assert profile_title_text, "Заголовок профиля должен быть виден в личном кабинете"

    def test_navigate_from_personal_account_to_constructor_via_button(
        self, driver, login_existing_user
    ):
        """Переход из личного кабинета в конструктор по кнопке 'Конструктор'."""
        go_to_personal_account(driver)

        click_element(driver, MainPage.CONSTRUCTOR_BUTTON)

        constructor_title_text = get_element_text(
            driver, MainPage.CONSTRUCTOR_TITLE
        )
        assert constructor_title_text, (
            "Заголовок конструктора должен быть виден после перехода из личного кабинета"
        )

    def test_navigate_from_personal_account_to_constructor_via_logo(
        self, driver, login_existing_user
    ):
        """Переход из личного кабинета в конструктор по клику на логотип."""
        go_to_personal_account(driver)

        click_element(driver, MainPage.LOGO)

        constructor_title_text = get_element_text(
            driver, MainPage.CONSTRUCTOR_TITLE
        )
        assert constructor_title_text, (
            "После клика по логотипу должен быть виден конструктор"
        )

    def test_logout_from_personal_account(self, driver, login_existing_user):
        """Выход из аккаунта по кнопке 'Выход' в личном кабинете."""
        go_to_personal_account(driver)

        click_element(driver, PersonalAccountPage.LOGOUT_BUTTON)

        login_title_text = get_element_text(driver, LoginPage.LOGIN_TITLE)
        assert login_title_text, "После выхода должна открыться форма входа"

        login_button_text = get_element_text(driver, LoginPage.LOGIN_BUTTON)
        assert login_button_text, "На форме входа должна быть кнопка 'Войти'"
