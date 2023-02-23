from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    return driver

