import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Homepage import Homepage
from pageObjects.Checkout import Checkout
from pageObjects.Shop import Shop
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import helper


@pytest.mark.usefixtures("setup")
class Test_e2e:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()

    logger = LogGen.loggen()

    def test_TC020_user_registration_and_checkout(self):
        self.driver.get(self.baseURL)
        self.hp = Homepage(self.driver)
        helper.clickOnElement_XPATH(self.driver, self.hp.button_dismiss_xpath)
        helper.clickOnElement_XPATH(self.driver, self.hp.button_myaccount_xpath)

        # VERIFY USER REGISTRATION
        self.lp = LoginPage(self.driver)
        self.setElementValue(self.driver, self.lp.textbox_reg_username_id, self.username)
        self.setElementValue(self.driver, self.lp.textbox_reg_email_id, self.email)
        self.setElementValue(self.driver, self.lp.textbox_password_id, self.password)
        helper.clickOnElement_XPATH(self.driver, self.lp.button_register_xpath)
        assert self.lp.is_logout_button_visible()

        # ADD ITEM TO THE CART
        self.hp.clickLogo()
        self.hp.clickFirstItem()
        self.shop = Shop(self.driver)
        self.shop.selectColor()
        self.shop.selectSize()
        self.shop.clickAddToCart()

        # CHECKOUT
        helper.clickOnElement_XPATH(self.driver, self.hp.button_checkout_xpath)
        self.ch = Checkout(self.driver)

        helper.setElementValue(self.driver, self.ch.textbox_name_id, ReadConfig.getData('firstName'))
        helper.setElementValue(self.driver, self.ch.textbox_surname_id, ReadConfig.getData('lastName'))
        self.ch.selectCountry(ReadConfig.getData('country'))
        helper.setElementValue(self.driver, self.ch.textbox_address_id, ReadConfig.getData('address'))
        helper.setElementValue(self.driver, self.ch.textbox_city_id, ReadConfig.getData('city'))
        helper.setElementValue(self.driver, self.ch.textbox_zip_id, ReadConfig.getData('zipCode'))
        helper.setElementValue(self.driver, self.ch.textbox_phone_id, ReadConfig.getData('phone'))
        helper.setElementValue(self.driver, self.ch.textbox_email_id, self.email)
        helper.clickOnElement_ID(self.driver, self.ch.checkbox_terms_id)
        self.driver.implicitly_wait(2)
        helper.clickOnElement_ID(self.driver, self.ch.button_place_order_id)

        # VERIFY CHECKOUT
        assert self.ch.is_order_received()
