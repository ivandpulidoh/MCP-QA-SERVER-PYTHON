from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base page class that all page objects will inherit from"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def wait_for_url(self, expected_url):
        """Wait for the URL to match the expected URL"""
        try:
            self.wait.until(lambda driver: expected_url in driver.current_url)
            return True
        except TimeoutException:
            return False
    
    def wait_for_element(self, locator):
        """Wait for an element to be present"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator):
        """Wait for an element to be clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))
