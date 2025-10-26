import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_page_locators import FaqPageLocators
from pages.base_page import BasePage

class FaqPage(BasePage):

    @allure.step("Прокрутить страницу до блока FAQ")
    def scroll_to_faq_section(self):
        faq_block = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".accordion"))
        )
        self.scroll_to_element((By.CSS_SELECTOR, ".accordion"))
        self.wait.until(EC.visibility_of(faq_block))

    @allure.step("Клик по вопросу №{index}")
    def click_question(self, index):
        self.scroll_to_faq_section()
        question_locator = (By.CSS_SELECTOR, FaqPageLocators.QUESTION.format(index))
        question = self.wait.until(EC.element_to_be_clickable(question_locator))
        question.click()

    @allure.step("Получение текста ответа для вопроса №{index}")
    def get_answer_text(self, index):
        answer_locator = (By.CSS_SELECTOR, FaqPageLocators.ANSWER.format(index))
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text