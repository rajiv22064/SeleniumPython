from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("This is Chrome driver test")
        driver = webdriver.Chrome(executable_path="C:\\BrowserExecutable\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
