import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.logo_page import LogoPage
from config import BASE_URL, YANDEX_URL

@allure.feature("Переходы по логотипам")
class TestClickLogo:

    @allure.title("Проверка перехода по логотипу 'Самокат'")
    def test_click_scooter_logo_redirects_to_main(self, driver):
        logo = LogoPage(driver)
        logo.click_order_top()
        logo.click_scooter_logo()
        assert logo.check_current_url(BASE_URL), "Переход по логотипу 'Самокат' не открыл главную страницу"

    @allure.title("Проверка открытия Дзена по логотипу 'Яндекс'")
    def test_click_yandex_logo_opens_dzen(self, driver):
        logo = LogoPage(driver)
        logo.click_yandex_logo()
        logo.switch_to_new_tab_and_wait_url(YANDEX_URL)
        assert YANDEX_URL in driver.current_url, f"Ожидался переход на {YANDEX_URL}"
