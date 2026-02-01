from selenium.webdriver.common.by import By


BASE_URL = "https://stellarburgers.education-services.ru/"


# главная страница
class MainPage:
    """Локаторы главной страницы"""

    # кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти в аккаунт')]",
    )

    # кнопка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[contains(text(), 'Личный Кабинет')]",
    )

    # логотип в шапке
    LOGO = (
        By.XPATH,
        "//div[contains(@class, 'AppHeader_header__logo')]",
    )

    # кнопка "Конструктор" в шапке
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[contains(text(), 'Конструктор')]",
    )

    # заголовок "Соберите бургер" на главной
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//h1[contains(text(), 'Соберите бургер')]",
    )


# страница входа
class LoginPage:
    """Локаторы страницы входа"""

    # поле ввода Email
    EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(., 'Email')]/following-sibling::input",
    )

    # поле ввода Пароль
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(., 'Пароль')]/following-sibling::input",
    )

    # кнопка "Войти"
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти')]",
    )

    # ссылка "Зарегистрироваться"
    REGISTER_LINK = (
        By.XPATH,
        "//a[contains(., 'Зарегистрироваться')]",
    )

    # ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[contains(., 'Восстановить пароль')]",
    )

    # заголовок формы "Вход"
    LOGIN_TITLE = (
        By.XPATH,
        "//h2[contains(text(), 'Вход')]",
    )


# страница регистрации
class RegistrationPage:
    """Локаторы страницы регистрации"""

    # поле "Имя"
    NAME_INPUT = (
        By.XPATH,
        "//label[contains(., 'Имя')]/following-sibling::input",
    )

    # поле "Email"
    EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(., 'Email')]/following-sibling::input",
    )

    # поле "Пароль"
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(., 'Пароль')]/following-sibling::input",
    )

    # кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Зарегистрироваться')]",
    )

    # ссылка "Войти" под формой регистрации
    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a.Auth_link__1fOlj[href='/login']",
    )

    # сообщение об ошибке пароля
    ERROR_MESSAGE = (
        By.XPATH,
        "//fieldset[3]//p[contains(@class, 'input__error')]",
    )


# страница восстановления пароля
class ForgotPasswordPage:
    """Локаторы страницы восстановления пароля"""

    # ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a.Auth_link__1fOlj[href='/login']",
    )


# личный кабинет
class PersonalAccountPage:
    """Локаторы личного кабинета"""

    # кнопка "Выход"
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Выход')]",
    )

    # ссылка/заголовок профиля
    PROFILE_TITLE = (
        By.XPATH,
        "//a[contains(@class, 'Account_link') and contains(@href, '/profile')]",
    )


# конструктор
class ConstructorPage:
    """Локаторы разделов конструктора"""

    # вкладка "Булки"
    BUNS_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Булки')]/parent::div",
    )

    # вкладка "Соусы"
    SAUCES_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Соусы')]/parent::div",
    )

    # вкладка "Начинки"
    FILLINGS_TAB = (
        By.XPATH,
        "//span[contains(text(), 'Начинки')]/parent::div",
    )

    # активная вкладка конструктора
    ACTIVE_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current')]",
    )
