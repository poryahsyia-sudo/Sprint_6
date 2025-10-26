import pytest
import allure
from pages.order_page import OrderPage
from test_data import ORDER_USERS
from locators.order_page_locators import OrderPageLocators
from config import DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


@allure.suite("Тест оформления заказа")
class TestOrderFlow:

    @pytest.mark.parametrize("user", ORDER_USERS)
    @allure.title("Оформление заказа через  кнопку 'Заказать'")
    def test_order_scooter_positive(self, driver, order_button, test_data): 
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        if order_button == "top":
            base_page.click_order_top()
        else:
            base_page.click_order_bottom()
        order_page.fill_name(test_data["name"])
        order_page.fill_surname(test_data["surname"])
        order_page.fill_address(test_data["address"])
        order_page.select_metro_station(test_data["metro"])
        order_page.fill_phone(test_data["phone"])
        order_page.click_next_button()
        order_page.fill_date_and_select_rental_period(test_data["date"], "сутки")
        order_page.fill_comment(test_data["comment"])
        order_page.click_order_button()
        order_page.confirm_order()
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_POPUP)
        )
        success_text = driver.find_element(*OrderPageLocators.ORDER_SUCCESS_POPUP).text
        assert "Заказ оформлен" in success_text, "Окно успешного заказа не появилось"