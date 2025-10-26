from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from config import DEFAULT_TIMEOUT


class OrderPage(BasePage):

    def fill_first_step(self, first_name, last_name, address, metro, phone):
        """Заполнение первого шага формы заказа"""
        wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)

        wait.until(EC.presence_of_element_located(OrderPageLocators.FIRST_NAME_FIELD)).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

        # Выбор станции метро
        metro_field = self.driver.find_element(*OrderPageLocators.METRO_FIELD)
        metro_field.click()
        wait.until(EC.presence_of_all_elements_located(OrderPageLocators.METRO_OPTION))[0].click()

        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_second_step(self, date, period, color, comment):
        """Заполнение второго шага формы заказа"""
        wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)

        # Ввод даты
        date_field = wait.until(EC.element_to_be_clickable(OrderPageLocators.DATE_FIELD))
        date_field.click()

        # Дождаться календаря и выбрать число
        wait.until(EC.visibility_of_element_located(OrderPageLocators.DATEPICKER))
        date_cell = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{date}']")
        date_cell.click()

        # Выбор периода аренды
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_OPTION(period))).click()

        # Выбор цвета
        self.driver.find_element(*OrderPageLocators.COLOR_CHECKBOX(color)).click()

        # Комментарий
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)

        # Клик по кнопке "Заказать"
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def confirm_order(self):
        """Подтверждение заказа"""
        wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)
        wait.until(EC.element_to_be_clickable(OrderPageLocators.YES_BUTTON)).click()

    def is_order_confirmed(self):
        """Проверка, что заказ успешно оформлен"""
        wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)
        try:
            wait.until(EC.visibility_of_element_located(OrderPageLocators.STATUS_MODAL))
            return True
        except TimeoutException:
            return False
