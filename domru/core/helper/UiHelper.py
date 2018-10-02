from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException


class UiHelper:

    def __init__(self, driver):
        self.driver = driver

    # Проверка элементов - видимость на странице
    def waitVisibleElementByID(self, expectedElement):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, expectedElement)))

    def waitVisibleElementByXPATH(self, expectedElement):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, expectedElement)))

    def waitVisibleElementByCSS_SELECTOR(self, expectedElement):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, expectedElement)))


    # Проверка элементов на кликабельность
    def elementIsClickableByID(self, clickableElement):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, clickableElement)))

    def elementIsClickableByXPATH(self, clickableElement):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, clickableElement)))

    def elementIsClickableByCSS_SELECTOR(self, clickableElement):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, clickableElement)))


    # Получить элемент
    def getElement(self, locator):
        locators = {By.ID, By.XPATH, By.CSS_SELECTOR, By.NAME, By.TAG_NAME, By.CLASS_NAME, By.LINK_TEXT}
        for loc in locators:
            try:
                return self.driver.find_element(loc, locator)
            except(NoSuchElementException, InvalidSelectorException):
                pass
        raise ValueError("Локатор не найден: " + locator)

    # Не работает!!!
    def waitVisibleElement(self, expectedElement):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((self.getElement(expectedElement))))

    # Не работает!!!
    def elementIsClickable(self, clickableElement):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((self.getElement(clickableElement))))
