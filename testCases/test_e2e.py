import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Homepage import Homepage
from pageObjects.Checkout import Checkout
from pageObjects.Shop import Shop
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_e2e:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()

    logger = LogGen.loggen()

    def setElementValue(self, element_id, value):
        element = self.driver.find_element(By.ID, element_id)
        element.clear()
        element.send_keys(value)

    def test_TC020_user_registration_and_checkout(self):
        self.driver.get(self.baseURL)
        self.hp = Homepage(self.driver)
        self.hp.clickDismiss()
        self.hp.clickMyAccount()

        # VERIFY USER REGISTRATION
        self.lp = LoginPage(self.driver)
        self.lp.setRegUsername(self.username)
        #self.setElementValue(self.lp.textbox_reg_username_id, self.username)

        self.lp.setRegEmail(self.email)
        self.lp.setRegPassword(self.password)
        self.lp.clickRegister()
        if self.lp.is_logout_button_visible():
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_registration.png")
            assert False

        # ADD ITEM TO THE CART
        self.hp.clickLogo()
        self.hp.clickFirstItem()
        self.shop = Shop(self.driver)
        self.shop.selectColor()
        self.shop.selectSize()
        self.shop.clickAddToCart()

        # CHECKOUT
        self.hp.clickCheckout()
        self.ch = Checkout(self.driver)
        self.ch.setFirstName(ReadConfig.getData('firstName'))
        self.ch.setLastName(ReadConfig.getData('lastName'))
        self.ch.selectCountry(ReadConfig.getData('country'))
        self.ch.setAddress(ReadConfig.getData('address'))
        self.ch.setCity(ReadConfig.getData('city'))
        self.ch.setZipCode(ReadConfig.getData('zipCode'))
        self.ch.setPhone(ReadConfig.getData('phone'))
        self.ch.setEmail(self.email)
        self.ch.clickCheckbox()
        self.driver.implicitly_wait(2)
        self.ch.clickPlaceOrder()

        # VERIFY CHECKOUT
        if self.ch.is_order_received():
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_registration.png")
