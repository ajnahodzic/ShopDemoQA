from selenium.webdriver.common.by import By

def clickOnElement_ByXpath(driver, xpath):
        driver.find_element(By.XPATH, xpath).click()