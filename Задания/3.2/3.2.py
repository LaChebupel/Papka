import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.selenium
class TestUnit(unittest.TestCase):
    def test_one(self):

        browser = webdriver.Chrome(executable_path="/path/to/chromedriver")
        link = "https://suninjuly.github.io/registration1.html"
        browser.get(link)

        fname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.first_class input")
        fname.send_keys("a")

        tname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
        tname.send_keys("b")

        email = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.third_class input")
        email.send_keys("asd@gmail.com")

        phone = browser.find_element(By.CSS_SELECTOR, "form div.second_block div.form-group.first_class input")
        phone.send_keys("+79999999999")

        adress = browser.find_element(By.CSS_SELECTOR, "form div.second_block div.form-group.second_class input")
        adress.send_keys("Jopa street")

if __name__ == "__main__":
    unittest.main()