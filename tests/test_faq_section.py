import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.faq_page import FaqPage
from locators.faq_page_locators import FaqPageLocators
from config import DEFAULT_TIMEOUT

#Проверка корректности отображения FAQ вопросов и ответов
class TestFaqSection:
    def _get_answer_text_from_dom(self, driver, index):
        answer_locator = (By.CSS_SELECTOR, FaqPageLocators.ANSWER.format(index))
        elem = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(answer_locator)
        )
        return elem.get_attribute("textContent").strip()

    def _get_answer_text_visible(self, driver, index):
        answer_locator = (By.CSS_SELECTOR, FaqPageLocators.ANSWER.format(index))
        elem = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return elem.text.strip()

    def test_question_1(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 1)
        page.click_question(1)
        actual = self._get_answer_text_visible(driver, 1)
        assert expected == actual, "Текст ответа для вопроса 1 не совпадает с текстом в коде страницы"

    def test_question_2(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 2)
        page.click_question(2)
        actual = self._get_answer_text_visible(driver, 2)
        assert expected == actual, "Текст ответа для вопроса 2 не совпадает с текстом в коде страницы"

    def test_question_3(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 3)
        page.click_question(3)
        actual = self._get_answer_text_visible(driver, 3)
        assert expected == actual, "Текст ответа для вопроса 3 не совпадает с текстом в коде страницы"

    def test_question_4(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 4)
        page.click_question(4)
        actual = self._get_answer_text_visible(driver, 4)
        assert expected == actual, "Текст ответа для вопроса 4 не совпадает с текстом в коде страницы"

    def test_question_5(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 5)
        page.click_question(5)
        actual = self._get_answer_text_visible(driver, 5)
        assert expected == actual, "Текст ответа для вопроса 5 не совпадает с текстом в коде страницы"

    def test_question_6(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 6)
        page.click_question(6)
        actual = self._get_answer_text_visible(driver, 6)
        assert expected == actual, "Текст ответа для вопроса 6 не совпадает с текстом в коде страницы"

    def test_question_7(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 7)
        page.click_question(7)
        actual = self._get_answer_text_visible(driver, 7)
        assert expected == actual, "Текст ответа для вопроса 7 не совпадает с текстом в коде страницы"

    def test_question_8(self, driver):
        page = FaqPage(driver)
        expected = self._get_answer_text_from_dom(driver, 8)
        page.click_question(8)
        actual = self._get_answer_text_visible(driver, 8)
        assert expected == actual, "Текст ответа для вопроса 8 не совпадает с текстом в коде страницы"
