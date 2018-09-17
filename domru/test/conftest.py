import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def setUp(request):
    chromeDriver = webdriver.Chrome(executable_path="/chromedriver")
    chromeDriver.implicitly_wait(5)
    chromeDriver.get("http://tvnew.domru.ru/")
    yield chromeDriver
    chromeDriver.close()
