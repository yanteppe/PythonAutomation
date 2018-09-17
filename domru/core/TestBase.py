# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class TestBase:

    def setup_method(self):
        self.driver = webdriver.Chrome("/chromedriver")
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        driver = self.driver
        self.driver.close()

    def getUrl(self, url):
        self.driver.get(url)