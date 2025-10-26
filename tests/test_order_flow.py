import pytest
import allure
from pages.order_page import OrderPage
from test_data import ORDER_USERS
from pages.base_page import BasePage
from config import DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators

@allure.suite("Тест оформления заказа")
class TestOrderFlow:
    @pytest.mark.parametrize("order_button", ["top", "bottom"])
    @pytest.mark.parametrize("user", ORDER_USERS)
    @allure.title("Оформление заказа через кнопку 'Заказать'")
    def test_order_scooter_positive(self, driver, order_button, user): 
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        if order_button == "top":
            base_page.scroll_into_view_and_click(OrderPageLocators.ORDER_BUTTON_TOP)
        else:
            base_page.scroll_into_view_and_click(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        order_page.fill_name(user["name"])
        order_page.fill_surname(user["surname"])
        order_page.fill_address(user["address"])
        order_page.select_metro_station(user["metro"])
        order_page.fill_phone(user["phone"])
        order_page.click_next_button()
        order_page.fill_date_and_select_rental_period(user["date"], "сутки")
        order_page.select_scooter_color(OrderPageLocators.COLOR_BLACK)
        order_page.fill_comment(user["comment"])
        order_page.click_order_button()
        order_page.confirm_order()
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_POPUP)
        )
        success_text = driver.find_element(*OrderPageLocators.ORDER_SUCCESS_POPUP).text
        assert "Заказ оформлен" in success_text, "Окно успешного заказа не появилось"