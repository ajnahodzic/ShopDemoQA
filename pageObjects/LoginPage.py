from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    textbox_reg_username_id = "reg_username"
    textbox_reg_password_id = "reg_password"
    textbox_reg_email_id = "reg_email"
    button_register_xpath = "//*[@id='customer_login']/div[2]/form/p[4]/button"
    button_login_xpath = "//*[@id='customer_login']/div[1]/form/p[3]/button"
    message_login_error_xpath = "//*[@id='post-8']/div/div/div[1]/ul/li"
    button_logout_xpath = "//*[@id='post-8']/div/div/nav/ul/li[6]/a"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def setRegUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_reg_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_reg_username_id).send_keys(username)

    def setRegEmail(self, password):
        self.driver.find_element(By.ID, self.textbox_reg_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_reg_email_id).send_keys(password)

    def setRegPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_reg_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_reg_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.button_register_xpath).click()

    def is_logout_button_visible(self):
        return self.driver.find_element(By.XPATH, self.button_logout_xpath).is_displayed()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()