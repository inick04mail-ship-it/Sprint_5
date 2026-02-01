import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import MainPage, ConstructorPage, BASE_URL


class TestConstructor:
    """Тесты конструктора бургеров без авторизации"""

    def open_main_page(self, driver):
        """Открывает главную страницу и ждёт загрузку конструктора."""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPage.CONSTRUCTOR_TITLE)
        )

    def get_active_tab_text(self, driver):
        """Возвращает текст активной вкладки конструктора."""
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPage.ACTIVE_TAB)
        )
        return active_tab.find_element(By.XPATH, ".//span").text

    def test_navigate_to_buns_section(self, driver):
        """
        Переход к разделу 'Булки'.
        По умолчанию активна вкладка 'Булки' — просто проверяем это.
        """
        self.open_main_page(driver)

        active_tab_text = self.get_active_tab_text(driver)
        assert active_tab_text == "Булки", f"Активная вкладка должна быть 'Булки', а не '{active_tab_text}'"

    def test_navigate_to_sauces_section(self, driver):
        """
        Переход к разделу 'Соусы'.
        Кликаем по span с текстом 'Соусы' и проверяем, что вкладка стала активной.
        """
        self.open_main_page(driver)

        sauces_span = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Соусы']")
            )
        )
        sauces_span.click()

        active_tab_text = self.get_active_tab_text(driver)
        assert active_tab_text == "Соусы", f"Активная вкладка должна быть 'Соусы', а не '{active_tab_text}'"

    def test_navigate_to_fillings_section(self, driver):
        """
        Переход к разделу 'Начинки'.
        Кликаем по span с текстом 'Начинки' и проверяем, что вкладка стала активной.
        """
        self.open_main_page(driver)

        fillings_span = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Начинки']")
            )
        )
        fillings_span.click()

        active_tab_text = self.get_active_tab_text(driver)
        assert active_tab_text == "Начинки", f"Активная вкладка должна быть 'Начинки', а не '{active_tab_text}'"
