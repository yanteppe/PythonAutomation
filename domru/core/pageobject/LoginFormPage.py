from selenium.webdriver.common.by import By


class LoginFormPage:

    def __init__(self, driver):
        self.driver = driver

    def openLoginForm(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.menu__link:nth-child(1)").click()

    def clickCitySelectionButton(self):
        self.driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/a").click()

    def inputUserName(self, inputUsername):
        self.driver.find_element_by_id("loginform-username").clear()
        self.driver.find_element_by_id("loginform-username").send_keys(inputUsername)

    def inputPassword(self, inputPassword):
        self.driver.find_element_by_id("loginform-password").clear()
        self.driver.find_element_by_id("loginform-password").send_keys(inputPassword)

    def clickSignInButton(self):
        self.driver.find_element(By.XPATH, "//*[@id='modal-auth-form']/div[5]/button/span").click()

    def checkBoxRememberMe(self):
        self.driver.find_element_by_xpath("//*[@id='modal-auth-form']/div[6]/div/label").click()


    # Восстановлене пароля
    def clickForgotPassButton(self):
        self.driver.find_element_by_xpath("//*[@id='modal-auth-form']/div[3]/a/span").click()

    # Восстановление пароля - поле ввода
    def inputRecoveryField(self, inputRecoveryField):
        self.driver.find_element_by_xpath("//*[@id='authrecoveryform-username']").clear()
        self.driver.find_element_by_xpath("//*[@id='authrecoveryform-username']").send_keys(inputRecoveryField)

    # Восстановление пароля - кнопка "Далее"
    def clickRecoveryButtonNext(self):
        self.driver.find_element_by_xpath("//*[@id='modal-auth-recovery-form']//button/span").click()
