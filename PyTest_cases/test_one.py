import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestForm:
    def form(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Alisa") #Имя
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Panina") #Фамилия
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("Panina@gmail.com") #Почта
        browser.find_element(By.CSS_SELECTOR, ".second_block .first_class input").send_keys("+79999999999") #Номер
        browser.find_element(By.CSS_SELECTOR, ".second_block .second_class input").send_keys("Moscow city") #Город
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click() #Кнопка

        welcome = browser.find_element(By.TAG_NAME, "h1").text
        
        return welcome
    
    def test_one(self):
        link = "https://suninjuly.github.io/registration1.html"
        reg_rez = self.form(link)
        assert reg_rez == "Congratulations! You have successfully registered!"
    
    def test_two(self):
        link = "https://suninjuly.github.io/registration2.html"
        reg_rez = self.form(link)
        assert reg_rez == "Congratulations! You have successfully registered!"

if __name__ == "__main__":
    TestForm().test_one()