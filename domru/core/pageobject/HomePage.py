from selenium.webdriver.common.by import By


class HomePage:
    elements = {"signInButton": "a.menu__link:nth-child(1)"}

    def __init__(self, driver):
        self.driver = driver

    def SignInButton(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.menu__link:nth-child(1)").click()
