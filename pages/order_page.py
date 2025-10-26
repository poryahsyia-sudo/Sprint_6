from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.order_page_locators import OrderPageLocators
from config import DEFAULT_TIMEOUT


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    # --- ДОБАВЛЕНО ---
    def open_main_page(self):
        """Открывает главную страницу"""
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_top_order_button(self):
        """Клик по верхней кнопке 'Заказать'"""
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text()='Заказать'])[1]"))
        )
        button.click()

    def click_bottom_order_button(self):
        """Клик по нижней кнопке 'Заказать'"""
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text()='Заказать'])[2]"))
        )
        button.click()
    # --- КОНЕЦ ДОБАВЛЕННОГО ---

    # Заполнение поля "Имя"
    def fill_name(self, name):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NAME_FIELD))
        field.clear()
        field.send_keys(name)

    # Заполнение поля "Фамилия"
    def fill_surname(self, surname):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.SURNAME_FIELD))
        field.clear()
        field.send_keys(surname)

    # Заполнение поля "Адрес"
    def fill_address(self, address):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ADDRESS_FIELD))
        field.clear()
        field.send_keys(address)

    # Выбор станции метро
    def select_metro_station(self, metro_name):
        metro_input = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_FIELD))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", metro_input)
        metro_input.click()

        metro_option = self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.METRO_OPTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", metro_option)
        metro_option = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_OPTION))
        metro_option.click()

    # Заполнение поля "Телефон"
    def fill_phone(self, phone):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.PHONE_FIELD))
        field.clear()
        field.send_keys(phone)

    # Переход на следующий шаг
    def click_next_button(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        button.click()

    # Заполнение даты и периода
    def fill_date_and_select_rental_period(self, date_text, period_text):
        date_field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DATE_FIELD))
        date_field.click()
        date_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{int(date_text.split('.')[0])}']"))
        )
        date_element.click()
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker")))
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-option' and text()='{period_text}']"))
        )
        option.click()

    # Выбор цвета самоката
    def select_scooter_color(self):
        color = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COLOR_BLACK))
        color.click()

    # Ввод комментария
    def fill_comment(self, comment):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COMMENT_FIELD))
        field.send_keys(comment)

    # Подтверждение заказа
    def click_order_button(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        button.click()

    # Подтверждение во всплывающем окне
    def confirm_order(self):
        confirm = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))
        confirm.click()

    # Проверка успешного окна
    def check_success_popup(self):
        popup = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_POPUP))
        return popup.is_displayed()
