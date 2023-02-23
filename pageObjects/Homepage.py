from selenium.webdriver.common.by import By


class Homepage:
    button_myaccount_xpath = "/html/body/div[2]/header/div[1]/div/ul[2]/li[2]/a"
    button_dismiss_xpath = "/html/body/p/a"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.button_myaccount_xpath).click()

    def clickDismiss(self):
        button = self.driver.find_element(By.XPATH, self.button_dismiss_xpath)
        if button.is_displayed():
            button.click()
