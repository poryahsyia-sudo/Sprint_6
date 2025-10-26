import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import BASE_URL

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(BASE_URL)

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO))
        logo.click()

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO))
        logo.click()

    @allure.step("Прокрутка до раздела FAQ")
    def scroll_to_faq_section(self):
        return self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Проверка, что открыт {expected_url}")
    def check_current_url(self, expected_url):
        return self.driver.current_url == expected_url
