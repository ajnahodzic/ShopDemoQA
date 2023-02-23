from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class Shop:
    item_first_xpath = "//*[@id='noo-site']/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[1]"
    button_addToCart_xpath = "/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/div/div[2]/button"
    dropdown_color_id = "pa_color"
    dropdown_size_id = "pa_size"
    button_view_cart_xpath = "//*[@id='noo-site']/div[2]/div/div/div[1]/div/a"
    name_of_item_xpath = "//*[@id='product-1162']/div[1]/div[2]/h1"

    def __init__(self, driver):
        self.driver = driver

    def clickFirstItem(self):
        self.driver.find_element(By.XPATH, self.item_first_xpath).click()

    def clickAddToCart(self):
        button = self.driver.find_element(By.XPATH, self.button_addToCart_xpath)
        ActionChains(self.driver).move_to_element(button)
        button.click()

    def selectSize(self):
        size_dropdown = self.driver.find_element(By.ID, self.dropdown_size_id)
        option = Select(size_dropdown)
        option.select_by_index(1)

    def selectColor(self):
        color_dropdown = self.driver.find_element(By.ID, self.dropdown_color_id)
        option = Select(color_dropdown)
        option.select_by_index(1)

    def clickViewCart(self):
        self.driver.find_element(By.XPATH, self.button_view_cart_xpath).click()

    def itemName(self):
        return self.driver.find_element(By.XPATH, self.name_of_item_xpath).text

