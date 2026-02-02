from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import DEFAULT_USER_NAME
from data_generators import generate_unique_email, generate_password
from locators import (
    MainPage,
    LoginPage,
    RegistrationPage,
    ForgotPasswordPage,
    PersonalAccountPage,
    ConstructorPage,
)
from urls import BASE_URL


def open_main_page(driver):
    """Открывает главную страницу и ждёт загрузку конструктора."""
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPage.CONSTRUCTOR_TITLE)
    )


def click_element(driver, locator):
    """Кликает по элементу с ожиданием кликабельности."""
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()
    return element


def get_element(driver, locator):
    """Возвращает найденный элемент после ожидания его присутствия."""
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locator)
    )
    return element


def get_element_text(driver, locator):
    """Возвращает текст элемента после ожидания его присутствия."""
    return get_element(driver, locator).text


def get_active_tab_text(driver):
    """Возвращает текст активной вкладки конструктора."""
    active_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPage.ACTIVE_TAB)
    )
    span_inside = active_tab.find_element(*ConstructorPage.TAB_SPAN)
    return span_inside.text


def go_to_login_from_main(driver):
    """Переход на форму логина с главной страницы по кнопке 'Войти в аккаунт'."""
    open_main_page(driver)
    click_element(driver, MainPage.LOGIN_BUTTON)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.LOGIN_TITLE)
    )


def go_to_registration_from_main(driver):
    """Переход на форму регистрации через главную страницу."""
    go_to_login_from_main(driver)
    click_element(driver, LoginPage.REGISTER_LINK)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegistrationPage.NAME_INPUT)
    )


def go_to_forgot_password_from_main(driver):
    """Переход на форму восстановления пароля через главную страницу."""
    go_to_login_from_main(driver)
    click_element(driver, LoginPage.FORGOT_PASSWORD_LINK)


def fill_registration_form(driver, user_data: dict):
    """Заполняет форму регистрации и жмёт 'Зарегистрироваться'."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegistrationPage.NAME_INPUT)
    ).send_keys(user_data["name"])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegistrationPage.EMAIL_INPUT)
    ).send_keys(user_data["email"])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegistrationPage.PASSWORD_INPUT)
    ).send_keys(user_data["password"])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPage.REGISTER_BUTTON)
    ).click()


def wait_for_login_form(driver):
    """Ожидает появления формы логина (заголовок 'Вход') и возвращает элемент заголовка."""
    return get_element(driver, LoginPage.LOGIN_TITLE)


def fill_login_form_and_submit(driver, email: str, password: str):
    """Заполняет форму логина и жмёт 'Войти'."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.PASSWORD_INPUT)
    ).send_keys(password)

    click_element(driver, LoginPage.LOGIN_BUTTON)


def wait_for_authorized_main_page(driver):
    """Ожидает, что пользователь авторизован и видна кнопка 'Личный кабинет'."""
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPage.PERSONAL_ACCOUNT_BUTTON)
    )


def go_to_personal_account(driver):
    """Переход в личный кабинет из шапки."""
    click_element(driver, MainPage.PERSONAL_ACCOUNT_BUTTON)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PersonalAccountPage.PROFILE_TITLE)
    )


def register_new_user(driver):
    """Регистрирует нового пользователя через UI и возвращает user_data."""
    user_data = {
        "name": DEFAULT_USER_NAME,
        "email": generate_unique_email(),
        "password": generate_password(),
    }

    go_to_registration_from_main(driver)
    fill_registration_form(driver, user_data)
    wait_for_login_form(driver)
    return user_data


def login_with_existing_user(driver, email, password):
    """Логинится под существующим пользователем."""
    open_main_page(driver)
    click_element(driver, MainPage.LOGIN_BUTTON)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.PASSWORD_INPUT)
    ).send_keys(password)

    click_element(driver, LoginPage.LOGIN_BUTTON)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPage.CONSTRUCTOR_TITLE)
    )


def get_registration_error_message(driver):
    """Возвращает элемент сообщения об ошибке на форме регистрации."""
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegistrationPage.ERROR_MESSAGE)
    )
