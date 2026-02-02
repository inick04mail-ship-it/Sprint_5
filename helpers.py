from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def get_active_tab_text(driver):
    """Возвращает текст активной вкладки конструктора."""
    active_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPage.ACTIVE_TAB)
    )
    # внутри активной вкладки лежит span с текстом
    return active_tab.find_element(By.TAG_NAME, "span").text


def go_to_login_from_main(driver):
    """Переход на форму логина с главной страницы по кнопке 'Войти в аккаунт'."""
    open_main_page(driver)
    login_button_main = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPage.LOGIN_BUTTON)
    )
    login_button_main.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.LOGIN_TITLE)
    )


def go_to_registration_from_main(driver):
    """Переход на форму регистрации через главную страницу."""
    go_to_login_from_main(driver)
    register_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPage.REGISTER_LINK)
    )
    register_link.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegistrationPage.NAME_INPUT)
    )


def go_to_forgot_password_from_main(driver):
    """Переход на форму восстановления пароля через главную страницу."""
    go_to_login_from_main(driver)
    forgot_password_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPage.FORGOT_PASSWORD_LINK)
    )
    forgot_password_link.click()


def fill_registration_form(driver, user_data: dict):
    """Заполняет форму регистрации и жмёт 'Зарегистрироваться'."""
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


def wait_for_login_form(driver):
    """Ожидает появления формы логина (заголовок 'Вход') и возвращает элемент заголовка."""
    login_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.LOGIN_TITLE)
    )
    return login_title


def fill_login_form_and_submit(driver, email: str, password: str):
    """Заполняет форму логина и жмёт 'Войти'."""
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPage.EMAIL_INPUT)
    )
    email_input.send_keys(email)

    password_input = driver.find_element(*LoginPage.PASSWORD_INPUT)
    password_input.send_keys(password)

    login_button = driver.find_element(*LoginPage.LOGIN_BUTTON)
    login_button.click()


def wait_for_authorized_main_page(driver):
    """Ожидает, что пользователь авторизован и видна кнопка 'Личный кабинет'."""
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
    )
    return personal_account_button


def go_to_personal_account(driver):
    """Переход в личный кабинет из шапки."""
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPage.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PersonalAccountPage.PROFILE_TITLE)
    )
