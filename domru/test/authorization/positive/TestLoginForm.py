from selenium import  webdriver
from domru.core.TestBase import TestBase
from domru.core.pageobject.LoginFormPage import LoginFormPage


class TestLoginForm(TestBase):

    def testLoginForm(self):
        self.getUrl("http://tvnew.domru.ru/")
        assert "Контентотека" in self.driver.title

        loginForm = LoginFormPage(self.driver)
        loginForm.openLoginForm()
        loginForm.inputUserName()

