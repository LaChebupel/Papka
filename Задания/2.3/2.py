from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = ("https://suninjuly.github.io/redirect_accept.html")
browser = webdriver.Chrome()
browser.get(link)

btn1 = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()

pg2 = browser.window_handles[1]
browser.switch_to.window(pg2)

num = browser.find_element(By.CSS_SELECTOR, "#input_value").text
num = float(num)

result = math.log(abs(12*math.sin(num)))
result = str(result)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(result)

btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
