# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from domru.core.helper.UiHelper import UiHelper
from domru.core.pageobject.LoginFormPage import LoginFormPage
from domru.core.pageobject.HomePage import HomePage


class TestLoginFormPositive(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.get("http://tvnew.domru.ru/")
        assert "Контентотека" in self.driver.title
        homePage = HomePage(self.driver)
        homePage.SignInButton()


    def testFormPositive_1(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("test")
        loginForm.inputPassword("test")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_2(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("test123")
        loginForm.inputPassword("test123")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_3(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("тест")
        loginForm.inputPassword("тест")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)


    def testFormPositive_4(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("test")
        loginForm.inputPassword("12345")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_5(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("tes")
        loginForm.inputPassword("tes")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_6(self):
        driver = self.driver
        loginForm = LoginFormPage(driver)
        uiHelper = UiHelper(driver)

        loginForm.inputUserName("te")
        loginForm.inputPassword("te")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
