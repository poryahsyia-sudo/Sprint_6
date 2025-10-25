from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from config import DEFAULT_TIMEOUT


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    # Прокрутка к нужному элементу, чтобы куки не перекрывали клики
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    # Клик по верхней кнопке «Заказать»
    def click_order_top(self):
        button = self.scroll_to_element(MainPageLocators.TOP_ORDER_BUTTON)
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.TOP_ORDER_BUTTON))
        button.click()

    # Клик по нижней кнопке «Заказать»
    def click_order_bottom(self):
        button = self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON))
        button.click()

    # Клик по логотипу самоката (возврат на главную)
    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO))
        logo.click()

    # Клик по логотипу Яндекса (открывается Дзен в новой вкладке)
    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO))
        logo.click()

    # Прокрутка до раздела FAQ
    def scroll_to_faq_section(self):
        return self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    # Проверка, что текущий URL соответствует ожидаемому
    def check_current_url(self, expected_url):
        return self.driver.current_url == expected_url
