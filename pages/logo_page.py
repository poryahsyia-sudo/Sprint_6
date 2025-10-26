from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.logo_page_locators import LogoPageLocators

class LogoPage(BasePage):

    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(LogoPageLocators.SCOOTER_LOGO))
        logo.click()

    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(LogoPageLocators.YANDEX_LOGO))
        logo.click()

    def check_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    def click_order_top(self):
        button = self.scroll_to_element(LogoPageLocators.TOP_ORDER_BUTTON)
        self.wait.until(EC.element_to_be_clickable(LogoPageLocators.TOP_ORDER_BUTTON))
        button.click()

    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(LogoPageLocators.SCOOTER_LOGO))
        logo.click()