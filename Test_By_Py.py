from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/registration1.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Alisa") #Имя
browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Panina") #Фамилия
browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("Panina@gmail.com") #Почта
browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input").send_keys("+79999999999") #Номер
browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input").send_keys("Moscow city") #Город
browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click() #Кнопка

browser.implicitly_wait(5)

welcome = browser.find_element(By.TAG_NAME, "h1").text

print (welcome)
