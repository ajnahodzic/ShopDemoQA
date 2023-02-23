from selenium.webdriver.common.by import By


class Cart:
    item_xpath = "//*[@id='post-6']/div/div/form/table/tbody/tr[1]/td[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def getItemName(self):
        return self.driver.find_element(By.XPATH, self.item_xpath).text
