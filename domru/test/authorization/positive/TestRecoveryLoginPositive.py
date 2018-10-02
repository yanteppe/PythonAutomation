# -*- coding: utf-8 -*-
import unittest

import pytest
from selenium import webdriver

from domru.core.helper.UiHelper import UiHelper
from domru.core.pageobject.LoginFormPage import LoginFormPage
from domru.core.pageobject.HomePage import HomePage

'''
Проверка формы авторизации - Восстановление пароля.
Позитивные проверки поля authrecoveryform-username.
'''
def testRecoveryField_contractNumber_1(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("test123")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_contractNumber_2(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("тест123")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_contractNumber_3(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("00000")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_contractNumber_4(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("№12345")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_phoneNumber_5(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("9191234567")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_phoneNumber_6(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("79191234567")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_phoneNumber_7(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("+79191234567")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_email_8(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("test@test.ru")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_email_9(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("test1@test.ru")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element

def testRecoveryField_email_10(setUp):
    loginForm = LoginFormPage(setUp)
    uiHelper = UiHelper(setUp)

    loginForm.openLoginForm()
    loginForm.clickForgotPassButton()
    loginForm.inputRecoveryField("test.test@test.ru")
    loginForm.clickRecoveryButtonNext()

    element = uiHelper.waitVisibleElementByXPATH(loginForm.elements["titleNotFindContract"])
    assert (element) == element