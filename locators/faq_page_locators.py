from selenium.webdriver.common.by import By

class FaqPageLocators:
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")
