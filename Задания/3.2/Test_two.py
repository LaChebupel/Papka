from selenium import webdriver
from selenium.webdriver.common.by import By
ink = "https://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("a")
mail = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("a@a")
phone = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input").send_keys("+79299299889")
adress = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input").send_keys("adress")
btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
