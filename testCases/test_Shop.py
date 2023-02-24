import pytest
from pageObjects.Shop import Shop
from pageObjects.Cart import Cart
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

    def test_TC008_validate_user_is_able_to_add_to_cart(self):
        self.logger.info("***** TEST Add To Cart *****")
        self.driver.get(self.baseURL + "/shop/")

        #SELECT ITEM
        self.shop = Shop(self.driver)
        helper.clickOnElement_XPATH(self.driver, self.shop.item_first_xpath)

        #SELECT SIZE AND COLOR
        self.shop.selectColor()
        self.shop.selectSize()
        chosen_item = self.shop.itemName()

        #ADD TO CART
        self.shop.clickAddToCart()

        #VALIDATE THE ITEM IS ADDED TO THE CART
        helper.clickOnElement_XPATH(self.driver, self.shop.button_view_cart_xpath)
        self.cart = Cart(self.driver)
        self.cart.getItemName()
        assert chosen_item in self.cart.getItemName()