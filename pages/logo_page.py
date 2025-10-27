import allure
from pages.base_page import BasePage
from locators.logo_page_locators import LogoPageLocators

class LogoPage(BasePage):

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.wait_and_click(LogoPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.wait_and_click(LogoPageLocators.YANDEX_LOGO)

    @allure.step("Проверить, что URL равен {expected_url}")
    def check_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    @allure.step("Кликнуть по верхней кнопке 'Заказать'")
    def click_order_top(self):
        self.scroll_into_view_and_click(LogoPageLocators.TOP_ORDER_BUTTON)