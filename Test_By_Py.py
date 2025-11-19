from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text

sum = int(num1) + int(num2)
sum_str = str(sum)
select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
select.select_by_value(sum_str)

sub = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
