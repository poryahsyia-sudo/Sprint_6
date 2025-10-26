from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT
from locators.logo_page_locators import LogoPageLocators
from locators.faq_page_locators import FaqPageLocators
from config import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open_page(self):
        self.driver.get(BASE_URL)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def wait_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def wait_and_send_keys(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
        return element

    def wait_and_press_enter(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys("\n")
        return element
    
    def scroll_to_faq_section(self):
        return self.scroll_to_element(FaqPageLocators.FAQ_SECTION)
    
    def scroll_into_view_and_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    