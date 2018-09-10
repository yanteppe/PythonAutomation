# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from domru.core.pageobject.HomePage import HomePage
from selenium.webdriver.common.by import By
from domru.core.pageobject.AutorizationFormPage import AutorizationFormPage


class TestAuthorizationForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://tvnew.domru.ru/")
        assert "Контентотека" in self.driver.title
        homePage = HomePage(self.driver)
        homePage.SignInButton()


    def test1(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)

        autorizationForm.inputUserName("test")
        autorizationForm.inputPassword("test")
        autorizationForm.signInButton()


    def test2(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)

        autorizationForm.inputUserName("test123")
        autorizationForm.inputPassword("test123")
        autorizationForm.signInButton()


    def test3(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)

        autorizationForm.inputUserName("тест")
        autorizationForm.inputPassword("тест")
        autorizationForm.signInButton()


    def test4(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)

        autorizationForm.inputUserName("test")
        autorizationForm.inputPassword("12345")
        autorizationForm.signInButton()


    def test5(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)

        autorizationForm.inputUserName("tes")
        autorizationForm.inputPassword("tes")
        autorizationForm.signInButton()

    def test6(self):
        driver = self.driver
        autorizationForm = AutorizationFormPage(driver)

        autorizationForm.inputUserName("te")
        autorizationForm.inputPassword("te")
        autorizationForm.signInButton()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
