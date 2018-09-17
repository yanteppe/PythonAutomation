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

    uiHelper.waitElement(pathToElement="//*[@id='modal-auth-form']/div[1]//p"
                                       and "//*[@id='modal-auth-form']/div[2]//p")
    assert (uiHelper) == uiHelper


def testPasswordEmpty_2(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("test")
    loginForm.inputPassword("")
    loginForm.clickSignInButton()

    uiHelper.waitElement(pathToElement="//*[@id='modal-auth-form']/div[2]//p")
    assert (uiHelper) == uiHelper


def testUsernameEmpty_3(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("")
    loginForm.inputPassword("test")
    loginForm.clickSignInButton()

    uiHelper.waitElement(pathToElement="//*[@id='modal-auth-form']/div[1]//p")
    assert (uiHelper) == uiHelper


def testInputOneSymbol_4(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName(".")
    loginForm.inputPassword(".")
    loginForm.clickSignInButton()

    uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
    assert (uiHelper) == uiHelper


def testInputInvalidCharacters_5(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.inputUserName("[|]'~<!--@%/*$%^&#*/()?>,|\.*/'")
    loginForm.inputPassword("[|]'~<!--@%/*$%^&#*/()?>,|\.*/'")
    loginForm.clickSignInButton()

    uiHelper.waitElement(pathToElement="//div[contains(@class, 'modal__paragraph form-error')]")
    assert (uiHelper) == uiHelper
