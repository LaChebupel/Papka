from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math

browser = webdriver.Chrome()
link = " https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
xint = float(x)

result = math.log(abs(12*math.sin(xint)))

result_str = str(result)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(result_str)

radio = browser.find_element(By.CSS_SELECTOR, "[for = robotsRule]")
box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")

browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", box)
box.click()

sub = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
