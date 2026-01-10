import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "https://habr.com"

class TestMainPage1():
    @classmethod
    def setup_class(self):
        print("\nstart browser for test")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\nquit browser for test")
        self.browser.quit()

    def test_quest_should_see_login_link(self):
        print("start test1")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#app > div > header > div.tm-page-width > div > span.tm-header__logo-wrap > a > svg")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("start test2")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#app > div > header > div.tm-page-width > div > button")

class TestMainPage2():
    def setup_method(self):
        print("\nstart browser for test")
        self.browser = webdriver.Chrome()
    
    def teardown_method(self):
        print("\nquit browser for test")
        self.browser.quit()

    def test_quest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#app > div > header > div.tm-page-width > div > span.tm-header__logo-wrap > a > svg")

    def test_guest_should_see_basket_link_on_the_main_page2(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#app > div > header > div.tm-page-width > div > button")