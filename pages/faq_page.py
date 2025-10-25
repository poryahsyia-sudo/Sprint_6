from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_page_locators import FaqPageLocators
from config import DEFAULT_TIMEOUT

class FaqPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def scroll_to_faq_section(self):
        # Ждём появления блока с вопросами на странице
        faq_block = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".accordion"))
        )
        # Прокручиваем страницу до блока с вопросами
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq_block)
        # Убеждаемся, что блок действительно видим
        self.wait.until(EC.visibility_of(faq_block))

    def click_question(self, index):
        # Прокручиваем страницу до раздела с вопросами
        self.scroll_to_faq_section()

        # Формируем локатор для нужного вопроса по индексу
        question_locator = (By.CSS_SELECTOR, FaqPageLocators.QUESTION.format(index))

        # Ждём появления вопроса в DOM
        question = self.wait.until(EC.presence_of_element_located(question_locator))

        # Прокручиваем страницу к нужному вопросу (центр экрана)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)

        # Ждём, пока вопрос станет кликабельным (чтобы его не перекрывала картинка)
        self.wait.until(EC.element_to_be_clickable(question_locator))

        # Кликаем по вопросу
        question.click()

    def get_answer_text(self, index):
        # Формируем локатор для ответа по индексу
        answer_locator = (By.CSS_SELECTOR, FaqPageLocators.ANSWER.format(index))

        # Ждём, пока ответ станет видимым
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))

        # Возвращаем текст ответа
        return answer.text