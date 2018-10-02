# -*- coding: utf-8 -*-
import unittest

import pytest
from selenium import webdriver

from domru.core.helper.UiHelper import UiHelper
from domru.core.pageobject.LoginFormPage import LoginFormPage
from domru.core.pageobject.HomePage import HomePage

'''
Проверка формы авторизации.
Негативные проверки полей username и password.
'''
def testUsernameAndPasswodEmpty_1(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("")
    loginForm.inputPassword("")
    loginForm.clickSignInButton()

    usernameErrorText = uiHelper.waitVisibleElementByXPATH(loginForm.elements["usernameMustBeFilledText"])
    assert (usernameErrorText) == usernameErrorText

    passErrorText = uiHelper.waitVisibleElementByXPATH(loginForm.elements["passMustBeFilledText"])
    assert (passErrorText) == passErrorText


def testPasswordEmpty_2(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("test")
    loginForm.inputPassword("")
    loginForm.clickSignInButton()

    passErrorText = uiHelper.waitVisibleElementByXPATH(loginForm.elements["passMustBeFilledText"])
    assert (passErrorText) == passErrorText


def testUsernameEmpty_3(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    errorLigonText = uiHelper.waitVisibleElementByXPATH(loginForm.elements["usernameMustBeFilledText"])
    assert (errorLigonText) == errorLigonText


def testInputOneSymbol_4(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName(".")
    loginForm.inputPassword(".")
    loginForm.clickSignInButton()

    errorLigonText = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (errorLigonText) == errorLigonText


def testInputInvalidCharacters_5(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("[|]'~<!--@%/*$%^&#*/()?>,|\.*/'")
    loginForm.inputPassword("[|]'~<!--@%/*$%^&#*/()?>,|\.*/'")
    loginForm.clickSignInButton()

    errorLigonText = uiHelper.waitVisibleElementByXPATH(loginForm.elements["errorLoginText"])
    assert (errorLigonText) == errorLigonText
