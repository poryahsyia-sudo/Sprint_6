from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from config import DEFAULT_TIMEOUT

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def fill_name(self, name):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NAME_FIELD))
        field.clear()
        field.send_keys(name)

    def fill_surname(self, surname):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.SURNAME_FIELD))
        field.clear()
        field.send_keys(surname)

    def fill_address(self, address):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ADDRESS_FIELD))
        field.clear()
        field.send_keys(address)

    def select_metro_station(self, metro_name):
        metro_input = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_FIELD))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", metro_input)
        metro_input.click()
        metro_option = self.wait.until(
            EC.presence_of_element_located((By.XPATH, OrderPageLocators.METRO_OPTION_TEMPLATE.format(metro_name)))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", metro_option)
        metro_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, OrderPageLocators.METRO_OPTION_TEMPLATE.format(metro_name)))
        )
        metro_option.click()

    def fill_phone(self, phone):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.PHONE_FIELD))
        field.clear()
        field.send_keys(phone)

    def click_next_button(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        button.click()

    def fill_date_and_select_rental_period(self, day, period_text):
        date_field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DATE_FIELD))
        date_field.click()
        date_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"))
        )
        date_element.click()
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        dropdown.click()
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, OrderPageLocators.RENTAL_PERIOD_OPTION_TEMPLATE.format(period_text)))
        )
        option.click()

    def select_scooter_color(self, color_locator):
        color_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(color_locator)
        )
        color_element.click()

    def fill_comment(self, comment):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COMMENT_FIELD))
        field.send_keys(comment)

    def click_order_button(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        button.click()

    def confirm_order(self):
        confirm = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))
        confirm.click()

    def check_success_popup(self):
        popup = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_POPUP))
        return popup.is_displayed()
