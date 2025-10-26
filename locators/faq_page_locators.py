from selenium.webdriver.common.by import By

class FaqPageLocators:
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")
