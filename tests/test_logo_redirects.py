import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class TestClickLogo:

    def test_click_scooter_logo_redirects_to_main(self, driver):
        main = MainPage(driver)
        main.click_order_top()
        main.click_scooter_logo()
        assert main.check_current_url("https://qa-scooter.praktikum-services.ru/"), \
            "Переход по логотипу 'Самокат' не открыл главную страницу"

    def test_click_yandex_logo_opens_dzen(self, driver):
        main = MainPage(driver)
        main.click_yandex_logo()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 15).until(
            EC.url_contains("https://dzen.ru/?yredirect=true")
        )
        current_url = driver.current_url
        assert "https://dzen.ru/?yredirect=true" in current_url, \
            f"Ожидался переход на Дзен, но открылось: {current_url}"