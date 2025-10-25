from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Button__ra12g')]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")