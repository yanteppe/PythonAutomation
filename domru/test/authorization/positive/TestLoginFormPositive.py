# -*- coding: utf-8 -*-

from domru.core.TestBase import TestBase
from domru.core.helper.UiHelper import UiHelper
from domru.core.pageobject.LoginFormPage import LoginFormPage

'''
Проверка формы авторизации.
Позитивные проверки полей username и password.
'''
class TestLoginFormPositive(TestBase):

    def testUsernameAndPassword_1(self):
        self.getUrl("http://tvnew.domru.ru/")
        uiHelper = UiHelper(self.driver)
        loginForm = LoginFormPage(self.driver)

        loginForm.openLoginForm()
        loginForm.inputUserName("test")
        loginForm.inputPassword("test")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        assert (uiHelper) == uiHelper

    def testUsernameAndPassword_2(self):
        self.getUrl("http://tvnew.domru.ru/")
        uiHelper = UiHelper(self.driver)
        loginForm = LoginFormPage(self.driver)

        loginForm.openLoginForm()
        loginForm.inputUserName("test123")
        loginForm.inputPassword("test123")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        assert (uiHelper) == uiHelper

    def testUsernameAndPassword_3(self):
        self.getUrl("http://tvnew.domru.ru/")
        uiHelper = UiHelper(self.driver)
        loginForm = LoginFormPage(self.driver)

        loginForm.openLoginForm()
        loginForm.inputUserName("тест")
        loginForm.inputPassword("тест")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        assert (uiHelper) == uiHelper

    def testUsernameAndPassword__4(self):
        self.getUrl("http://tvnew.domru.ru/")
        uiHelper = UiHelper(self.driver)
        loginForm = LoginFormPage(self.driver)

        loginForm.openLoginForm()
        loginForm.inputUserName("test")
        loginForm.inputPassword("12345")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        assert uiHelper == uiHelper

    def testUsernameAndPassword__5(self):
        self.getUrl("http://tvnew.domru.ru/")
        uiHelper = UiHelper(self.driver)
        loginForm = LoginFormPage(self.driver)

        loginForm.openLoginForm()
        loginForm.inputUserName("tes")
        loginForm.inputPassword("tes")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        assert uiHelper == uiHelper

    def testUsernameAndPassword__6(self):
        self.getUrl("http://tvnew.domru.ru/")
        uiHelper = UiHelper(self.driver)
        loginForm = LoginFormPage(self.driver)

        loginForm.openLoginForm()
        loginForm.inputUserName("te")
        loginForm.inputPassword("te")
        loginForm.clickSignInButton()

        uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
        assert uiHelper == uiHelper