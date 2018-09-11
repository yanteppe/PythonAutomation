# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from domru.core.helper.UiHelper import UiHelper
from domru.core.pageobject.LoginFormPage import LoginFormPage
from domru.core.pageobject.HomePage import HomePage


class TestLoginFormNegative(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.get("http://tvnew.domru.ru/")
        assert "Контентотека" in self.driver.title
        homePage = HomePage(self.driver)
        homePage.SignInButton()


    def usernameAndPasswodEmpty_1(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("")
        loginForm.inputPassword("")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//*[@id='modal-auth-form']/div[1]//p"
                                       and "//*[@id='modal-auth-form']/div[2]//p")
        self.assertTrue(uiHelper)


    def passwordEmpty_2(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("test")
        loginForm.inputPassword("")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//*[@id='modal-auth-form']/div[2]//p")
        self.assertTrue(uiHelper)


    def usernameEmpty_3(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("")
        loginForm.inputPassword("test")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//*[@id='modal-auth-form']/div[1]//p")
        self.assertTrue(uiHelper)

    def inputOneSymbol_4(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName(".")
        loginForm.inputPassword(".")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def inputInvalidCharacters_5(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("[|]'~<!--@%/*$%^&#*/()?>,|\.*/'")
        loginForm.inputPassword("[|]'~<!--@%/*$%^&#*/()?>,|\.*/'")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)


if __name__ == '__main__':
    unittest.main(TestLoginFormNegative)
