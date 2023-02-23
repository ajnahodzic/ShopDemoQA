import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.logger.info("***** TEST HOMEPAGE *****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepage.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.logger.info("***** TEST LOGIN *****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
