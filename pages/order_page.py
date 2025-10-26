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
    def fill_second_step(self, date: str, rental_period: str, scooter_color: str, comment: str):
        # Выбор даты
        self.wait_and_click(OrderPageLocators.DATE_FIELD)
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATEPICKER))

        # Клик по нужному числу, чтобы закрыть календарь
        date_cell = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{date}']")
        self.wait_and_click(date_cell)

        # Выбор срока аренды
        self.wait_and_click(OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_option = OrderPageLocators.RENTAL_PERIOD_OPTION(rental_period)
        self.wait_and_click(rental_option)

        # Выбор цвета
        color_checkbox = OrderPageLocators.COLOR_CHECKBOX(scooter_color)
        self.wait_and_click(color_checkbox)

        # Комментарий
        self.wait_and_send_keys(OrderPageLocators.COMMENT_FIELD, comment)

        # Кнопка "Заказать"
        self.wait_and_click(OrderPageLocators.ORDER_BUTTON)

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
