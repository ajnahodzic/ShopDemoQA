import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Homepage import Homepage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_MyAccount:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()

    logger = LogGen.loggen()

    def test_registration(self):
        self.logger.info("***** TEST REGISTRATION *****")
        self.driver.get(self.baseURL)
        self.hp = Homepage(self.driver)
        self.hp.clickDismiss()
        self.hp.clickMyAccount()

        self.lp = LoginPage(self.driver)
        self.lp.setRegUsername(self.username)
        self.lp.setRegEmail(self.email)
        self.lp.setRegPassword(self.password)
        self.lp.clickRegister()

        if self.lp.is_logout_button_visible():
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_registration.png")
            self.driver.close()
            assert False

    def test_login(self):
        self.logger.info("***** TEST LOGIN *****")
        self.driver.get(self.baseURL)

        self.hp = Homepage(self.driver)
        self.hp.clickDismiss()
        self.hp.clickMyAccount()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        if self.lp.is_logout_button_visible():
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False


