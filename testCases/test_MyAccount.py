import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Homepage import Homepage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import helper

@pytest.mark.usefixtures("setup")
class Test_MyAccount:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()

    logger = LogGen.loggen()

    def test_TC001_user_registration_with_new_valid_data(self):
        self.logger.info("***** TEST REGISTRATION *****")
        self.driver.get(self.baseURL)
        self.hp = Homepage(self.driver)
        helper.clickOnElement_XPATH(self.driver, self.hp.button_dismiss_xpath)
        helper.clickOnElement_XPATH(self.driver, self.hp.button_myaccount_xpath)

        self.lp = LoginPage(self.driver)
        self.setElementValue(self.driver, self.lp.textbox_reg_username_id, self.username)
        self.setElementValue(self.driver, self.lp.textbox_reg_email_id, self.email)
        self.setElementValue(self.driver, self.lp.textbox_password_id, self.password)
        helper.clickOnElement_XPATH(self.driver, self.lp.button_register_xpath)
        assert self.lp.is_logout_button_visible()


    def test_TC003_user_login_of_registered_user(self):
        self.logger.info("***** TEST LOGIN *****")
        self.driver.get(self.baseURL)
        self.hp = Homepage(self.driver)
        helper.clickOnElement_XPATH(self.driver, self.hp.button_dismiss_xpath)
        helper.clickOnElement_XPATH(self.driver, self.hp.button_myaccount_xpath)

        self.lp = LoginPage(self.driver)
        self.setElementValue(self.driver, self.lp.textbox_username_id, self.username)
        self.setElementValue(self.driver, self.lp.textbox_password_id, self.password)
        helper.clickOnElement_XPATH(self.driver, self.lp.button_login_xpath)
        assert self.lp.is_logout_button_visible()



