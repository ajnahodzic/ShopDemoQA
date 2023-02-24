from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Homepage:
    button_myaccount_xpath = "/html/body/div[2]/header/div[1]/div/ul[2]/li[2]/a"
    button_dismiss_xpath = "/html/body/p/a"
    button_checkout_xpath = "//a[contains(text(),'Checkout')]"
    logo_class = "custom-logo"
    item_first_xpath = "//*[@id='noo-site']/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/h3/a"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.button_myaccount_xpath).click()

    def clickCheckout(self):
        self.driver.find_element(By.XPATH, self.button_checkout_xpath).click()


    def clickLogo(self):
        button = self.driver.find_element(By.CLASS_NAME, self.logo_class)
        if button.is_displayed():
            button.click()

    def clickDismiss(self):
        button = self.driver.find_element(By.XPATH, self.button_dismiss_xpath)
        if button.is_displayed():
            button.click()

    def clickFirstItem(self):
        item = self.driver.find_element(By.XPATH, self.item_first_xpath)
        ActionChains(self.driver).move_to_element(item)
        item.click()