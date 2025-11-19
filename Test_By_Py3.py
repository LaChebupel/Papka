from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

dir = os.getcwd()

file_path = os.path.join(dir, 'Sasha_jopa.txt')

file_str = str(file_path)

print(os.path.isfile(file_str))
print(file_str)

send = browser.find_element(By.CSS_SELECTOR, "#file")
send.send_keys(file_str)
