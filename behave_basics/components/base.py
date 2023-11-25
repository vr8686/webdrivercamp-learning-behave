import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Base:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click(self, xpath: str):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, xpath))).click()

    def find_element(self, xpath: str):
        element = self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        time.sleep(0.2)
        return element

    def find_present_element(self, xpath: str):
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
        time.sleep(0.2)
        return element

    def search_for_item(self, search_item):
        search_bar_xpath = ('//div[@class="styles__SearchWrapper-sc-1ywf0d0-0 bpBcjs"]'
                     '//input[contains(@placeholder, "What can we help you find?")]')
        product_list_xpath = '//div[contains(@class, "ProductListGrid")]'
        locator = self.find_element(search_bar_xpath)
        locator.send_keys(search_item)
        locator.send_keys(Keys.RETURN)
        self.wait.until(ec.presence_of_element_located((By.XPATH, product_list_xpath)))

    def get_text(self, xpath: str):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath))).text

    def verify_header_contains(self, keyword: str):
        header = '//h1[@data-test="page-title"]'
        element_text = self.get_text(header)
        if keyword in element_text.lower():
            print(f'Success. The header contains "{keyword}".')
        else:
            print(f'Mismatch. The header DOES NOT contain "{keyword}"')
