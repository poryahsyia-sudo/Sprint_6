import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config import BASE_URL, YANDEX_URL

@allure.feature("Переходы по логотипам")
class TestClickLogo:

    @allure.title("Проверка перехода по логотипу 'Самокат'")
    def test_click_scooter_logo_redirects_to_main(self, driver):
        Base = BasePage(driver)
        Base.click_order_top()
        Base.click_scooter_logo()
        assert Base.check_current_url(BASE_URL), "Переход по логотипу 'Самокат' не открыл главную страницу"

    @allure.title("Проверка открытия Дзена по логотипу 'Яндекс'")
    def test_click_yandex_logo_opens_dzen(self, driver):
        Base = BasePage(driver)
        Base.click_yandex_logo()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 15).until(EC.url_contains(YANDEX_URL))
        assert YANDEX_URL in driver.current_url, f"Ожидался переход на {YANDEX_URL}"