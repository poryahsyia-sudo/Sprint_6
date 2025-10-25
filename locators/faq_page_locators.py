from selenium.webdriver.common.by import By

class FaqPageLocators:
    QUESTION = ".accordion__item:nth-child({})"
    ANSWER = ".accordion__item:nth-child({}) .accordion__panel"
