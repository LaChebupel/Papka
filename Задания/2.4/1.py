from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

text = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element(By.ID, "book")
button.click()

value = browser.find_element(By.ID, "input_value").text
value = float(value)

result = math.log(abs(12*math.sin(value)))
result = str(result)

form = browser.find_element(By.ID, "answer")
form.send_keys(result)

sub = browser.find_element(By.ID, "solve")
sub.click()
