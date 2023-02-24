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
    test_name = request.node.name
    driver.save_screenshot(".\\screenshots\\" + test_name + ".png")
    driver.close()
    return driver

