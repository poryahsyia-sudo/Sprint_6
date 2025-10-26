import pytest
import allure
from pages.faq_page import FaqPage

@allure.feature("Тестирование FAQ Раздела")
class TestFaqSection:

    @pytest.mark.parametrize("index", [1, 2, 3, 4, 5, 6, 7, 8])
    @allure.title("Проверка раскрытия вопроса №{index}")
    def test_faq_question_display(self, driver, index):
        page = FaqPage(driver)
        page.scroll_to_faq_section()
        expected = page.get_answer_text(index)  # получаем текст из DOM
        page.click_question(index)
        actual = page.get_answer_text(index)    # получаем отображаемый текст
        assert expected == actual, f"Ответ для вопроса {index} не совпадает"