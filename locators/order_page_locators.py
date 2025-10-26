from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая часть формы
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN_FIRST = (By.XPATH, "//li[@class='select-search__row']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая часть формы
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATEPICKER = (By.XPATH, "//div[contains(@class, 'react-datepicker__month-container')]")  # ✅ добавляем это
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    RENTAL_PERIOD_OPTION = lambda period: (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
    COLOR_CHECKBOX = lambda color: (By.XPATH, f"//label[text()='{color}']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    STATUS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
