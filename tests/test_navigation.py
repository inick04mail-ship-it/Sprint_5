import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MainPage,
    PersonalAccountPage,
    LoginPage,
    BASE_URL,
)


class TestNavigation:
    """Тесты навигации для уже авторизованного пользователя"""

    def test_navigate_to_personal_account(self, driver, login_existing_user):
        """
        Переход в личный кабинет при нажатии на 'Личный кабинет'.
        """
        # 1. Пользователь уже залогинен 

        # 2. Нажимаем кнопку "Личный кабинет"
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # 3. Проверяем, что мы в личном кабинете
        profile_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPage.PROFILE_TITLE)
        )
        assert profile_title.is_displayed(), "Заголовок профиля должен быть виден в личном кабинете"

    def test_navigate_from_personal_account_to_constructor_via_button(self, driver, login_existing_user):
        """
        Переход из личного кабинета в конструктор по кнопке 'Конструктор'.
        """
        # 1. Пользователь уже залогинен

        # 2. Переходим в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPage.PROFILE_TITLE)
        )

        # 3. Нажимаем кнопку "Конструктор" в шапке
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        # 4. Проверяем, что вернулись к конструктору
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPage.CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed(), "Заголовок конструктора должен быть виден после перехода из личного кабинета"

    def test_navigate_from_personal_account_to_constructor_via_logo(self, driver, login_existing_user):
        """
        Переход из личного кабинета в конструктор по клику на логотип.
        """
        # 1. Пользователь уже залогинен

        # 2. Переходим в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPage.PROFILE_TITLE)
        )

        # 3. Нажимаем на логотип Stellar Burgers
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.LOGO)
        )
        logo.click()

        # 4. Проверяем, что вернулись к конструктору
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPage.CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed(), "После клика по логотипу должен быть виден конструктор"

    def test_logout_from_personal_account(self, driver, login_existing_user):
        """
        Выход из аккаунта по кнопке 'Выход' в личном кабинете.
        """
        # 1. Пользователь уже залогинен

        # 2. Переходим в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPage.PROFILE_TITLE)
        )

        # 3. Нажимаем кнопку "Выход"
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountPage.LOGOUT_BUTTON)
        )
        logout_button.click()

        # 4. Проверяем, что появилась форма входа (заголовок "Вход" и кнопка "Войти")
        login_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.LOGIN_TITLE)
        )
        assert login_title.is_displayed(), "После выхода должна открыться форма входа"

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPage.LOGIN_BUTTON)
        )
        assert login_button.is_displayed(), "На форме входа должна быть кнопка 'Войти'"