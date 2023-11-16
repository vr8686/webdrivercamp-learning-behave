from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Base:
    SEARCHBAR = ('//div[@class="styles__SearchWrapper-sc-1ywf0d0-0 bpBcjs"]'
                 '//input[contains(@placeholder, "What can we help you find?")]')
    H1HEADER = '//h1[@data-test="page-title"]'
    PRODUCTLIST = '//div[@class="styles__ProductListGridFadedLoading-sc-u8zdb1-0"]'

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def find_element(self, xpath):
        element = self.wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        return element

    def search_for_item(self, search_item):
        locator = self.find_element(self.SEARCHBAR)
        locator.send_keys(search_item)
        locator.send_keys(Keys.RETURN)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.PRODUCTLIST)))

    def get_text(self, locator):
        text = self.wait.until(ec.visibility_of_element_located((By.XPATH, locator))).text
        return text

    def verify_element_contains(self, element: str, keyword: str):
        element_text = self.get_text(element)
        print(f'Checking if {element_text} contains word \"{keyword}\"...')
        if keyword in element_text.lower():
            print(f'Success. The element contains \"{keyword}\".')
        else:
            print(f'Mismatch. The element DOES NOT contain \"{keyword}\"')
