import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHuman():
    def test_youtube(self, youtube):
        print ("Hello")