import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestUnit(unittest.TestCase):
    def test_b(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("a")
        mail = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("a@a")
        phone = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input").send_keys("+79299299889")
        adress = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input").send_keys("adress")
        btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    def test_a(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.first_class input").send_keys("a")
        tname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input").send_keys("b")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.third_class input").send_keys("asd@gmail.com")
        phone = browser.find_element(By.CSS_SELECTOR, "form div.second_block div.form-group.first_class input").send_keys("+79999999999")
        adress = browser.find_element(By.CSS_SELECTOR, "form  div.second_block div.form-group.second_class input").send_keys("Jopa street")
        btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()


if __name__ == "__main__":
    unittest.main()