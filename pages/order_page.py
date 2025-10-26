import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        self.wait_and_send_keys(OrderPageLocators.NAME_FIELD, first_name)
        self.wait_and_send_keys(OrderPageLocators.SURNAME_FIELD, last_name)
        self.wait_and_send_keys(OrderPageLocators.ADDRESS_FIELD, address)
        self.wait_and_click(OrderPageLocators.METRO_FIELD)
        metro_option = (By.XPATH, OrderPageLocators.METRO_OPTION_TEMPLATE.format(metro_station))
        self.scroll_to_element(metro_option)
        self.wait_and_click(metro_option)
        self.wait_and_send_keys(OrderPageLocators.PHONE_FIELD, phone)
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй части формы заказа: дата={date}, срок={rental_period}")
    def fill_second_step(self, date: str, rental_period: str, scooter_color: str, comment: str):
        self.wait_and_click(OrderPageLocators.DATE_FIELD)
        self.wait_and_send_keys(OrderPageLocators.DATE_FIELD, date)
        self.wait_and_press_enter(OrderPageLocators.DATE_FIELD)
        self.wait_and_click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_option = (By.XPATH, OrderPageLocators.RENTAL_PERIOD_OPTION_TEMPLATE.format(rental_period))
        self.scroll_to_element(rental_option)
        self.wait_and_click(rental_option)

        color = scooter_color.lower()
        if color == "black":
            self.wait_and_click(OrderPageLocators.COLOR_BLACK)
        elif color in ("grey", "gray"):
            self.wait_and_click(OrderPageLocators.COLOR_GREY)
        self.wait_and_send_keys(OrderPageLocators.COMMENT_FIELD, comment)
        self.wait_and_click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.wait_and_click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверка успешного оформления заказа")
    def check_success_message(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_POPUP))
            return True
        except Exception:
            return False