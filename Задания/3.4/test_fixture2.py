import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.habr.com"

@pytest.fixture
def browser():
    print("\nbrowser started")
    browser = webdriver.Chrome()
    return browser

class TestMainPage1():
    def test_one(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#app > div > header > div > div > span.tm-header__logo-wrap > a > svg > use")
    
    def test_two(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#app > div > header > div.tm-page-width > div > button")