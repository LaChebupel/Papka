import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup_module():
    link = "www.youtube.com"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)