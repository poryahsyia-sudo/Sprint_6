import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from config import DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestOrderFlow:

    @pytest.mark.parametrize("order_button", ["top", "bottom"])
    @pytest.mark.parametrize("user_data", [
        {
            "name": "Анастасия",
            "surname": "Иванова",
            "address": "г. Москва, ул. Ленина, д. 5",
            "metro": "Сокольники",
            "phone": "+79998887766",
            "date": "25.10.2025",
            "comment": "Позвонить за 5 минут до прибытия",
        },
        {
            "name": "Мария",
            "surname": "Петрова",
            "address": "г. Москва, Гоголя пр., 10",
            "metro": "Технопарк",
            "phone": "+79995554433",
            "date": "30.10.2025",
            "comment": "Позвонить заранее",
        },
    ])

#Тест проверка позитивного сценария оформления заказа: Проверка появления окна успешного оформления
    def test_order_scooter_positive(self, driver, order_button, user_data): 
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        if order_button == "top":
            main_page.click_order_top()
        else:
            main_page.click_order_bottom()
        order_page.fill_name(user_data["name"])
        order_page.fill_surname(user_data["surname"])
        order_page.fill_address(user_data["address"])
        order_page.select_metro_station(user_data["metro"])
        order_page.fill_phone(user_data["phone"])
        order_page.click_next_button()
        order_page.fill_date_and_select_rental_period(user_data["date"], "сутки")
        order_page.fill_comment(user_data["comment"])
        order_page.click_order_button()
        order_page.confirm_order()
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_POPUP)
        )
        success_text = driver.find_element(*OrderPageLocators.ORDER_SUCCESS_POPUP).text
        assert "Заказ оформлен" in success_text, "Окно успешного заказа не появилось"