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
        order_page = OrderPage(driver)
        order_page.click_top_order_button()
        order_page.fill_first_step(
            user["first_name"],
            user["last_name"],
            user["address"],
            user["metro_station"],
            user["phone"]
        )
        order_page.fill_second_step(
            "2025-10-30",
            "двое суток",
            "чёрный жемчуг",
            user["comment"]
        )
        order_page.confirm_order()
        assert order_page.check_success_message(), "Сообщение об успешном заказе не появилось"

    @pytest.mark.parametrize("user", ORDER_USERS)
    @allure.title("Оформление заказа через нижнюю кнопку 'Заказать'")
    def test_order_from_bottom_button(self, driver, user):
        main = MainPage(driver)
        main.open_main_page()
        order_page = OrderPage(driver)
        order_page.click_bottom_order_button()
        order_page.fill_first_step(
            user["first_name"],
            user["last_name"],
            user["address"],
            user["metro_station"],
            user["phone"]
        )
        order_page.fill_second_step(
            "2025-10-31",
            "один день",
            "серая безысходность",
            user["comment"]
        )
        order_page.confirm_order()
        assert order_page.check_success_message(), "Сообщение об успешном заказе не появилось"
