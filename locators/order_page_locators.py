from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION_TEMPLATE = "//div[@class='select-search__select']//div[text()='{0}']"
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION_TEMPLATE = "//div[contains(@class,'Dropdown-menu')]//div[text()='{0}']"
    COLOR_BLACK = (By.ID, "black")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Заказать') and contains(@class,'Button_Middle')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_POPUP = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
    ORDER_SUCCESS_POPUP = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
