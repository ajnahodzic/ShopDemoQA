from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class Checkout:
    button_myaccount_xpath = "/html/body/div[2]/header/div[1]/div/ul[2]/li[2]/a"
    button_dismiss_xpath = "/html/body/p/a"
    textbox_name_id = "billing_first_name"
    textbox_surname_id = "billing_last_name"
    textbox_address_id = "billing_address_1"
    textbox_city_id = "billing_city"
    textbox_zip_id = "billing_postcode"
    textbox_phone_id = "billing_phone"
    textbox_email_id = "billing_email"
    checkbox_terms_id = "terms"
    dropdown_country_id = "billing_country"
    button_place_order_id = "place_order"
    message_order_received_class = "woocommerce-thankyou-order-received"

    def __init__(self, driver):
        self.driver = driver

    def selectCountry(self, country):
        country_dropdown = Select(self.driver.find_element(By.ID, self.dropdown_country_id))
        country_dropdown.select_by_visible_text(country)

    def is_order_received(self):
        return self.driver.find_element(By.CLASS_NAME, self.message_order_received_class).is_displayed()

    def tickCheckbox(self):
        self.driver.find_element(By.ID, self.checkbox_terms_id).click()

    def clickPlaceOrder(self):
        self.driver.find_element(By.ID, self.button_place_order_id).click()