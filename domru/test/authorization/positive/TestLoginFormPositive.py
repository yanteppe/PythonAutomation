# -*- coding: utf-8 -*-

from domru.core.helper.UiHelper import UiHelper
from domru.core.pageobject.HomePage import HomePage
from domru.core.pageobject.LoginFormPage import LoginFormPage

'''
Проверка формы авторизации.
Позитивные проверки полей username и password.
'''
def testUsernameAndPassword_login_1(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("test")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_login_2(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()

    loginForm.inputUserName("test123")
    loginForm.inputPassword("test123")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_login_3(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("тест")
    loginForm.inputPassword("тест")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_login_4(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("test")
    loginForm.inputPassword("12345")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_login_5(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("tes")
    loginForm.inputPassword("tes")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_login_6(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("te")
    loginForm.inputPassword("te")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_contractNumber_7(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("№test12345")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_contractNumber_8(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("№12345")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_contractNumber_9(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("00000")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_email_10(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("test@test.ru")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_email_11(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("test1@test.ru")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element


def testUsernameAndPassword_email_12(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("test.test@test.ru")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (element) == element
