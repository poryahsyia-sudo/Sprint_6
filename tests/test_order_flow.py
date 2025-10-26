import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import ORDER_USERS

@allure.feature("Проверка оформления заказа")
class TestOrderFlow:

    @allure.title("Оформление заказа через верхнюю кнопку 'Заказать'")
    def test_order_from_top_button(self, driver):
        main = MainPage(driver)
        main.open_main_page()

        order_page = OrderPage(driver)
        order_page.click_top_order_button()

        order_page.fill_first_step(
            ORDER_USERS["first_name"],
            ORDER_USERS["last_name"],
            ORDER_USERS["address"],
            ORDER_USERS["metro_station"],
            ORDER_USERS["phone"]
        )
        order_page.fill_second_step(
            date="10.10.2025",
            rental_period="двое суток",
            scooter_color="black",
            comment=ORDER_USERS["comment"]
        )
        order_page.confirm_order()

        assert order_page.check_success_message(), "Сообщение об успешном заказе не отображается"

    @allure.title("Оформление заказа через нижнюю кнопку 'Заказать'")
    def test_order_from_bottom_button(self, driver):
        main = MainPage(driver)
        main.open_main_page()

        order_page = OrderPage(driver)
        order_page.click_bottom_order_button()

        order_page.fill_first_step(
            ORDER_USERS["first_name"],
            ORDER_USERS["last_name"],
            ORDER_USERS["address"],
            ORDER_USERS["metro_station"],
            ORDER_USERS["phone"]
        )
        order_page.fill_second_step(
            date="12.10.2025",
            rental_period="сутки",
            scooter_color="grey",
            comment=ORDER_USERS["comment"]
        )
        order_page.confirm_order()

        assert order_page.check_success_message(), "Сообщение об успешном заказе не отображается"