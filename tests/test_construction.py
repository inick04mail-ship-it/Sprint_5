import pytest

from helpers import open_main_page, get_active_tab_text, click_element
from locators import ConstructorPage


class TestConstructor:
    """Тесты конструктора бургеров без авторизации."""

    def test_default_tab_is_buns(self, driver):
        """По умолчанию активна вкладка 'Булки'."""
        open_main_page(driver)

        active_tab_text = get_active_tab_text(driver)
        assert active_tab_text == "Булки", (
            f"Активная вкладка должна быть 'Булки', а не '{active_tab_text}'"
        )

    @pytest.mark.parametrize(
        "tab_locator, expected_text",
        [
            (ConstructorPage.SAUCES_TAB, "Соусы"),
            (ConstructorPage.FILLINGS_TAB, "Начинки"),
        ],
    )
    def test_navigate_to_sections(self, driver, tab_locator, expected_text):
        """Переход между разделами конструктора: 'Соусы', 'Начинки'."""
        open_main_page(driver)

        click_element(driver, tab_locator)

        active_tab_text = get_active_tab_text(driver)
        assert active_tab_text == expected_text, (
            f"Активная вкладка должна быть '{expected_text}', а не '{active_tab_text}'"
        )
