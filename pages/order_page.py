import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        button = self.scroll_to_element(MainPageLocators.TOP_ORDER_BUTTON)
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.TOP_ORDER_BUTTON))
        button.click()

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        button = self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON))
        button.click()

    @allure.step("Заполнение первой части формы заказа: {first_name} {last_name}")
    def fill_first_step(self, first_name: str, last_name: str, address: str, metro_station: str, phone: str):
        self.wait_and_send_keys(OrderPageLocators.FIRST_NAME_FIELD, first_name)
        self.wait_and_send_keys(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.wait_and_send_keys(OrderPageLocators.ADDRESS_FIELD, address)

        self.wait_and_click(OrderPageLocators.METRO_FIELD)
        self.wait.until(EC.presence_of_all_elements_located(OrderPageLocators.METRO_OPTION))[0].click()

        self.wait_and_send_keys(OrderPageLocators.PHONE_FIELD, phone)
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй части формы заказа: дата={date}, срок={rental_period}")
    def fill_second_step(self, date, rental_period, color, comment):
        # Ввод даты и закрытие календаря выбором даты
        self.wait_and_click(OrderPageLocators.DATE_FIELD)
        date_field = self.wait_for_element(OrderPageLocators.DATE_FIELD)
        date_field.send_keys(Keys.CONTROL + "a")
        date_field.send_keys(Keys.BACKSPACE)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)  # календарь закроется после выбора даты

        # Выбор периода аренды
        self.wait_and_click(OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_option = OrderPageLocators.RENTAL_PERIOD_OPTION(rental_period)
        try:
            self.wait.until(EC.element_to_be_clickable(rental_option)).click()
        except TimeoutException:
            # иногда список не успевает открыться — пробуем ещё раз
            self.wait_and_click(OrderPageLocators.RENTAL_PERIOD_FIELD)
            self.wait.until(EC.element_to_be_clickable(rental_option)).click()

        # Выбор цвета
        color_checkbox = OrderPageLocators.COLOR_CHECKBOX(color)
        self.wait_and_click(color_checkbox)

        # Комментарий
        self.wait_and_send_keys(OrderPageLocators.COMMENT_FIELD, comment)

        # Клик по кнопке "Заказать" с гарантией клика
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        order_button = self.wait_for_element(OrderPageLocators.ORDER_BUTTON)
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        order_button.click()

        
    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.wait_and_click(OrderPageLocators.YES_BUTTON)

    @allure.step("Проверка успешного оформления заказа")
    def check_success_message(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.STATUS_MODAL))
            return True
        except TimeoutException:
            return False
