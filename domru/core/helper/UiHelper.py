from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UiHelper:

    def __init__(self, driver):
        self.driver = driver

    def waitElement(self, pathToElement):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, pathToElement)))

#     def getElement(self, locator):
#         return self.driver.find_element(by=locator)
#
#     def clickElement(self, locator):
#         return self.getElement(locator).click()
