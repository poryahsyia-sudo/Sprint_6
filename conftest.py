import pytest
from selenium import webdriver
from config import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
