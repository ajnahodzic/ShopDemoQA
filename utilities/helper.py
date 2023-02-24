from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def clickOnElement_XPATH(driver, element_xpath):
        element = driver.find_element(By.XPATH, element_xpath)
        if element.is_displayed():
                element.click()

def clickOnElement_ID(driver, element_id):
        element = driver.find_element(By.ID, element_id).click()
        if element.is_displayed():
                element.click()

def setElementValue(driver, element_id, value):
        element = driver.find_element(By.ID, element_id)
        ActionChains(driver).move_to_element(element)
        element.clear()
        element.send_keys(value)