from selenium.webdriver.common.by import By
from domru.core.helper.UiHelper import UiHelper
from domru.test.conftest import setUp

class LoginFormPage:
    elements = {
        "openLoginForm": 'a.menu__link:nth-child(1)',
        "clickCitySelectionButton": '/html/body/div[7]/div/div[2]/a',
        "userName": "loginform-username",
        "password": 'loginform-password',
        "signInButton": "//*[@id='modal-auth-form']/div[5]/button/span",
        "checkBoxRememberMe": "//*[@id='modal-auth-form']/div[6]/div/label",
        "clickForgotPassButton": "//*[@id='modal-auth-form']/div[3]/a/span",
        "inputRecoveryField": "//*[@id='authrecoveryform-username']",
        "clickRecoveryButtonNext": "//*[@id='modal-auth-recovery-form']//button/span",

         # Тексты после заполнения формы
        "errorLoginText": "//div[contains(@class, 'modal__paragraph form-error')]",
        "titleNotFindContract": "/html/*/div[2]/*/div[1]",
        "usernameMustBeFilledText": "//*[@id='modal-auth-form']/div[1]/div/div/p",
        "passMustBeFilledText": "//*[@id='modal-auth-form']/div[2]//p"
    }

    def __init__(self, driver):
        self.driver = driver

    def openLoginForm(self):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByCSS_SELECTOR(self.elements["openLoginForm"])
        uiHelper.elementIsClickableByCSS_SELECTOR(self.elements["openLoginForm"])

        self.driver.find_element(By.CSS_SELECTOR, self.elements["openLoginForm"]).click()

    def clickCitySelectionButton(self):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByXPATH(self.elements["clickCitySelectionButton"])
        uiHelper.elementIsClickableByXPATH(self.elements["clickCitySelectionButton"])

        self.driver.find_element_by_xpath(self.elements["clickCitySelectionButton"]).click()

    def inputUserName(self, inputUsername):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByID(self.elements["userName"])
        uiHelper.elementIsClickableByID(self.elements["userName"])

        self.driver.find_element_by_id(self.elements["userName"]).clear()
        self.driver.find_element_by_id(self.elements["userName"]).send_keys(inputUsername)

    def inputPassword(self, inputPassword):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByID(self.elements["password"])
        uiHelper.elementIsClickableByID(self.elements["password"])

        self.driver.find_element_by_id(self.elements["password"]).clear()
        self.driver.find_element_by_id(self.elements["password"]).send_keys(inputPassword)

    def clickSignInButton(self):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByXPATH(self.elements["signInButton"])
        uiHelper.elementIsClickableByXPATH(self.elements["signInButton"])

        self.driver.find_element(By.XPATH, self.elements["signInButton"]).click()

    def checkBoxRememberMe(self):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByXPATH(self.elements["checkBoxRememberMe"])
        uiHelper.elementIsClickableByXPATH(self.elements["checkBoxRememberMe"])

        self.driver.find_element_by_xpath(self.elements["checkBoxRememberMe"]).click()

    # Восстановлене пароля
    def clickForgotPassButton(self):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByXPATH(self.elements["clickForgotPassButton"])
        uiHelper.elementIsClickableByXPATH(self.elements["clickForgotPassButton"])

        self.driver.find_element_by_xpath(self.elements["clickForgotPassButton"]).click()

    # Восстановление пароля - поле ввода
    def inputRecoveryField(self, inputRecoveryField):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByXPATH(self.elements["inputRecoveryField"])
        uiHelper.elementIsClickableByXPATH(self.elements["inputRecoveryField"])

        self.driver.find_element_by_xpath(self.elements["inputRecoveryField"]).clear()
        self.driver.find_element_by_xpath(self.elements["inputRecoveryField"]).send_keys(inputRecoveryField)

    # Восстановление пароля - кнопка "Далее"
    def clickRecoveryButtonNext(self):
        uiHelper = UiHelper(self.driver)
        uiHelper.waitVisibleElementByXPATH(self.elements["clickRecoveryButtonNext"])
        uiHelper.elementIsClickableByXPATH(self.elements["clickRecoveryButtonNext"])

        self.driver.find_element_by_xpath(self.elements["clickRecoveryButtonNext"]).click()
