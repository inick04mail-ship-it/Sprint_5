import pytest

from helpers import open_main_page, get_active_tab_text
from locators import ConstructorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestConstructor:
    """Тесты конструктора бургеров без авторизации."""

    @pytest.mark.parametrize(
        "tab_locator, expected_text, need_click",
        [
            # вкладка 'Булки' активна по умолчанию, клик не нужен
            (ConstructorPage.BUNS_TAB, "Булки", False),
            (ConstructorPage.SAUCES_TAB, "Соусы", True),
            (ConstructorPage.FILLINGS_TAB, "Начинки", True),
        ],
    )
    def test_navigate_to_sections(self, driver, tab_locator, expected_text, need_click):
        """
        Проверка переходов между разделами конструктора:
        'Булки', 'Соусы', 'Начинки'.
        """
        open_main_page(driver)

        if need_click:
            # Находим контейнер вкладки
            tab_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(tab_locator)
            )
            # Берём span внутри вкладки и кликаем именно по нему
            span_inside = tab_element.find_element(By.TAG_NAME, "span")
            span_inside.click()

        active_tab_text = get_active_tab_text(driver)
        assert (
            active_tab_text == expected_text
        ), f"Активная вкладка должна быть '{expected_text}', а не '{active_tab_text}'"
