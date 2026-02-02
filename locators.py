from selenium.webdriver.common.by import By


class MainPage:
    """Локаторы главной страницы"""

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти в аккаунт')]",
    )

    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[contains(text(), 'Личный Кабинет')]",
    )

    LOGO = (
        By.XPATH,
        "//div[contains(@class, 'AppHeader_header__logo')]",
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[contains(text(), 'Конструктор')]",
    )

    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//h1[contains(text(), 'Соберите бургер')]",
    )


class LoginPage:
    """Локаторы страницы входа"""

    EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(., 'Email')]/following-sibling::input",
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(., 'Пароль')]/following-sibling::input",
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти')]",
    )

    REGISTER_LINK = (
        By.XPATH,
        "//a[contains(., 'Зарегистрироваться')]",
    )

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[contains(., 'Восстановить пароль')]",
    )

    LOGIN_TITLE = (
        By.XPATH,
        "//h2[contains(text(), 'Вход')]",
    )


class RegistrationPage:
    """Локаторы страницы регистрации"""

    NAME_INPUT = (
        By.XPATH,
        "//label[contains(., 'Имя')]/following-sibling::input",
    )

    EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(., 'Email')]/following-sibling::input",
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(., 'Пароль')]/following-sibling::input",
    )

    REGISTER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Зарегистрироваться')]",
    )

    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a.Auth_link__1fOlj[href='/login']",
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "p.input__error",
    )


class ForgotPasswordPage:
    """Локаторы страницы восстановления пароля"""

    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a.Auth_link__1fOlj[href='/login']",
    )


class PersonalAccountPage:
    """Локаторы личного кабинета"""

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Выход')]",
    )

    PROFILE_TITLE = (
        By.XPATH,
        "//a[contains(@class, 'Account_link') and contains(@href, '/profile')]",
    )


class ConstructorPage:
    """Локаторы разделов конструктора"""

    BUNS_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Булки')]/parent::div",
    )

    SAUCES_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Соусы')]/parent::div",
    )

    FILLINGS_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Начинки')]/parent::div",
    )

    ACTIVE_TAB = (
        By.CSS_SELECTOR,
        "div.tab_tab_type_current__2BEPc",
    )

    TAB_SPAN = (By.TAG_NAME, "span")
