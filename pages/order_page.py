import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step("Заполнить поле 'Имя'")
    def fill_name(self, name):
        self.wait_and_send_keys(OrderPageLocators.NAME_FIELD, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def fill_surname(self, surname):
        self.wait_and_send_keys(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step("Заполнить поле 'Адрес'")
    def fill_address(self, address):
        self.wait_and_send_keys(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Выбрать станцию метро {metro_name}")
    def select_metro_station(self, metro_name):
        self.scroll_into_view_and_click(OrderPageLocators.METRO_FIELD)
        metro_option = (By.XPATH, OrderPageLocators.METRO_OPTION_TEMPLATE.format(metro_name))
        self.wait_and_click(metro_option)

    @allure.step("Заполнить поле 'Телефон'")
    def fill_phone(self, phone):
        self.wait_and_send_keys(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату {day} и период аренды '{period_text}'")
    def fill_date_and_select_rental_period(self, day, period_text):
        self.wait_and_click(OrderPageLocators.DATE_FIELD)
        date_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        self.wait_and_click(date_locator)
        self.wait_and_click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_option = (By.XPATH, OrderPageLocators.RENTAL_PERIOD_OPTION_TEMPLATE.format(period_text))
        self.wait_and_click(period_option)

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color_locator):
        self.wait_and_click(color_locator)

    @allure.step("Добавить комментарий для курьера")
    def fill_comment(self, comment):
        self.wait_and_send_keys(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self, locator):
        self.wait_and_click(locator)
        
    @allure.step("Подтвердить оформление заказа")
    def confirm_order(self):
        self.wait_and_click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить, что появилось окно успешного заказа")
    def check_success_popup(self):
        popup = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_POPUP))
        return popup.is_displayed()
