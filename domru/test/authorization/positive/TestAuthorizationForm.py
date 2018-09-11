# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from domru.core.helper.UiHelper import UiHelper
from domru.core.pageobject.AutorizationFormPage import AutorizationFormPage
from domru.core.pageobject.HomePage import HomePage


class TestAuthorizationForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.get("http://tvnew.domru.ru/")
        assert "Контентотека" in self.driver.title
        homePage = HomePage(self.driver)
        homePage.SignInButton()


    def testFormPositive_1(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)
        uiHelper = UiHelper(driver)

        autorizationForm.inputUserName("test")
        autorizationForm.inputPassword("test")
        autorizationForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_2(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)
        uiHelper = UiHelper(driver)

        autorizationForm.inputUserName("test123")
        autorizationForm.inputPassword("test123")
        autorizationForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_3(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)
        uiHelper = UiHelper(driver)

        autorizationForm.inputUserName("тест")
        autorizationForm.inputPassword("тест")
        autorizationForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)


    def testFormPositive_4(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)
        uiHelper = UiHelper(driver)

        autorizationForm.inputUserName("test")
        autorizationForm.inputPassword("12345")
        autorizationForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_5(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)
        uiHelper = UiHelper(driver)

        autorizationForm.inputUserName("tes")
        autorizationForm.inputPassword("tes")
        autorizationForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def testFormPositive_6(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)
        uiHelper = UiHelper(driver)

        autorizationForm.inputUserName("te")
        autorizationForm.inputPassword("te")
        autorizationForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        self.assertTrue(uiHelper)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
