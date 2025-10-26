from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первый шаг
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION_TEMPLATE = "//li[@class='select-search__row' and text()='{}']"
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Второй шаг 
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    RENTAL_PERIOD_OPTION_TEMPLATE = "//div[@class='Dropdown-option' and text()='{}']"
    COLOR_BLACK = (By.XPATH, "//label[text()='чёрный']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_POPUP = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Кнокпи
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

