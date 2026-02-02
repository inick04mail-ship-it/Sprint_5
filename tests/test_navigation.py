from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import go_to_personal_account
from locators import MainPage, PersonalAccountPage, LoginPage


class TestNavigation:
    """Тесты навигации для уже авторизованного пользователя."""

    def test_navigate_to_personal_account(self, driver, login_existing_user):
        """Переход в личный кабинет при нажатии на 'Личный кабинет'."""
        go_to_personal_account(driver)

        profile_title = driver.find_element(*PersonalAccountPage.PROFILE_TITLE)
        assert profile_title.is_displayed(), (
            "Заголовок профиля должен быть виден в личном кабинете"
        )

    def test_navigate_from_personal_account_to_constructor_via_button(
        self, driver, login_existing_user
    ):
        """Переход из личного кабинета в конструктор по кнопке 'Конструктор'."""
        go_to_personal_account(driver)

        constructor_button = driver.find_element(*MainPage.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        constructor_title = driver.find_element(*MainPage.CONSTRUCTOR_TITLE)
        assert constructor_title.is_displayed(), (
            "Заголовок конструктора должен быть виден после перехода из личного кабинета"
        )

    def test_navigate_from_personal_account_to_constructor_via_logo(
        self, driver, login_existing_user
    ):
        """Переход из личного кабинета в конструктор по клику на логотип."""
        go_to_personal_account(driver)

        logo = driver.find_element(*MainPage.LOGO)
        logo.click()

        constructor_title = driver.find_element(*MainPage.CONSTRUCTOR_TITLE)
        assert constructor_title.is_displayed(), (
            "После клика по логотипу должен быть виден конструктор"
        )

    def test_logout_from_personal_account(self, driver, login_existing_user):
        """Выход из аккаунта по кнопке 'Выход' в личном кабинете."""
        go_to_personal_account(driver)

        logout_button = driver.find_element(*PersonalAccountPage.LOGOUT_BUTTON)
        logout_button.click()

        # Ждём, пока появится форма входа (заголовок 'Вход')
        login_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.LOGIN_TITLE)
        )
        assert login_title.is_displayed(), (
            "После выхода должна открыться форма входа"
        )

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.LOGIN_BUTTON)
        )
        assert login_button.is_displayed(), (
            "На форме входа должна быть кнопка 'Войти'"
        )
