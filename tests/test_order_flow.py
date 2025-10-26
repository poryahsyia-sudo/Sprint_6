import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import ORDER_USERS


@allure.suite("Тест оформления заказа")
class TestOrderFlow:

    @pytest.mark.parametrize("user", ORDER_USERS)
    @allure.title("Оформление заказа через верхнюю кнопку 'Заказать'")
    def test_order_from_top_button(self, driver, user):
        main = MainPage(driver)
        main.open_main_page()
        main.click_top_order_button()

        order_page = OrderPage(driver)

        # --- Первый шаг ---
        order_page.fill_name(user["first_name"])
        order_page.fill_surname(user["last_name"])
        order_page.fill_address(user["address"])
        order_page.select_metro_station(user["metro_station"])
        order_page.fill_phone(user["phone"])
        order_page.click_next_button()

        # --- Второй шаг ---
        order_page.fill_date_and_select_rental_period("30.10.2025", "двое суток")
        order_page.select_scooter_color()
        order_page.fill_comment(user["comment"])
        order_page.click_order_button()
        order_page.confirm_order()

        assert order_page.check_success_popup(), "Сообщение об успешном заказе не появилось"

    @pytest.mark.parametrize("user", ORDER_USERS)
    @allure.title("Оформление заказа через нижнюю кнопку 'Заказать'")
    def test_order_from_bottom_button(self, driver, user):
        main = MainPage(driver)
        main.open_main_page()
        main.click_bottom_order_button()

        order_page = OrderPage(driver)

        # --- Первый шаг ---
        order_page.fill_name(user["first_name"])
        order_page.fill_surname(user["last_name"])
        order_page.fill_address(user["address"])
        order_page.select_metro_station(user["metro_station"])
        order_page.fill_phone(user["phone"])
        order_page.click_next_button()

        # --- Второй шаг ---
        order_page.fill_date_and_select_rental_period("31.10.2025", "один день")
        order_page.select_scooter_color()
        order_page.fill_comment(user["comment"])
        order_page.click_order_button()
        order_page.confirm_order()

        assert order_page.check_success_popup(), "Сообщение об успешном заказе не появилось"
