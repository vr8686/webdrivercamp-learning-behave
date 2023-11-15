from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Base:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def find_element(self, xpath):
        element = self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        return element

    def type_and_send_return(self, locator, search_item):
        locator = self.find_element(locator)
        locator.send_keys(search_item)
        locator.send_keys(Keys.RETURN)

    def get_text(self, locator):
        text = self.wait.until(ec.visibility_of_element_located((By.XPATH, locator))).text
        return text
