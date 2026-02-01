import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import ConstructorPage
from urls import BASE_URL


class TestConstructor:
    """Тесты конструктора бургеров без авторизации"""

    def open_main_page(self, driver):
        """Открывает главную страницу и ждёт загрузку конструктора."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ConstructorPage.BUNS_TAB)
        )

    def get_active_tab_text(self, driver):
        """Возвращает текст активной вкладки конструктора."""
        active_tab_span = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPage.ACTIVE_TAB)
        )
        return active_tab_span.text

    @pytest.mark.parametrize(
        "tab_locator, expected_text, need_click",
        [
            (ConstructorPage.BUNS_TAB, "Булки", False),   # по умолчанию уже активна
            (ConstructorPage.SAUCES_TAB, "Соусы", True),
            (ConstructorPage.FILLINGS_TAB, "Начинки", True),
        ],
    )
    def test_navigate_to_sections(self, driver, tab_locator, expected_text, need_click):
        """
        Проверка переходов между разделами конструктора:
        'Булки', 'Соусы', 'Начинки'.
        """
        self.open_main_page(driver)

        if need_click:
            # Находим контейнер вкладки
            tab_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(tab_locator)
            )
            # Берём span внутри вкладки и кликаем именно по нему
            span_inside = tab_element.find_element(By.TAG_NAME, "span")
            span_inside.click()

        active_tab_text = self.get_active_tab_text(driver)
        assert (
            active_tab_text == expected_text
        ), f"Активная вкладка должна быть '{expected_text}', а не '{active_tab_text}'"
