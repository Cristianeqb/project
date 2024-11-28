from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Clique em um elemento."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        """Digite em um campo."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Obtenha o texto de um elemento."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

