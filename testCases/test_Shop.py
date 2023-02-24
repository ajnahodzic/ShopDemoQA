import pytest
from pageObjects.Shop import Shop
from pageObjects.Cart import Cart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_MyAccount:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()

    logger = LogGen.loggen()

    def test_TC008_validate_add_to_cart(self):
        self.logger.info("***** TEST Add To Cart *****")
        self.driver.get(self.baseURL + "/shop/")

        #SELECT ITEM
        self.shop = Shop(self.driver)
        self.shop.clickFirstItem()
        self.driver.implicitly_wait(2)

        #SELECT SIZE AND COLOR
        self.shop.selectColor()
        self.shop.selectSize()
        chosen_item = self.shop.itemName()

        #ADD TO CART
        self.shop.clickAddToCart()

        #VERIFY CART
        self.shop.clickViewCart()
        self.cart = Cart(self.driver)
        self.cart.getItemName()

        if chosen_item in self.cart.getItemName():
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addToCart.png")
            assert False