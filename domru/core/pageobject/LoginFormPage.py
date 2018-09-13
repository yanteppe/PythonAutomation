from selenium.webdriver.common.by import By

class LoginFormPage:

    def __init__(self, driver):
        self.driver = driver

    def openLoginForm(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.menu__link:nth-child(1)").click()

    def citySelectionButton(self):
        self.driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/a").click()

    def inputUserName(self, inputUsername):
        self.driver.find_element_by_id("loginform-username").clear()
        self.driver.find_element_by_id("loginform-username").send_keys(inputUsername)

    def inputPassword(self, inputPassword):
        self.driver.find_element_by_id("loginform-password").clear()
        self.driver.find_element_by_id("loginform-password").send_keys(inputPassword)

    def forgotPassButton(self):
        self.driver.find_element_by_xpath("//*[@id='modal-auth-form']/div[3]/a/span").click()

    def clickSignInButton(self):
        self.driver.find_element(By.XPATH, "//*[@id='modal-auth-form']/div[5]/button/span").click()

    def checkBoxRememberMe(self):
        self.driver.find_element_by_xpath("//*[@id='modal-auth-form']/div[6]/div/label").click()

    def passRecoveryField(self, inputField):
        self.driver.find_element_by_xpath("//input[@id='authrecoveryform-username']").clear()
        self.driver.find_element_by_xpath("//input[@id='authrecoveryform-username']").send_keys(inputField)

