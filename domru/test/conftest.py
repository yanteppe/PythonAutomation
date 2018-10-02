import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def setUp(request):
    chromeDriver = webdriver.Chrome(executable_path="/chromedriver")
    chromeDriver.implicitly_wait(5)
    chromeDriver.get("http://tvnew.domru.ru/")
    yield chromeDriver
    chromeDriver.quit()

# @pytest.yield_fixture(params=[("test"), ("test123"), ("тест")])
# def usernameData(request):
#     yield request.param
#
# @pytest.yield_fixture(params=[("test"), ("test123"), ("тест")])
# def passwordData(request):
#     yield request.param