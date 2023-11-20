import time

from behave_basics.components.base import Base
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class GiftsPage(Base):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def select_option_in_section(self, section, option):
        section_title = f'''//h2//span[contains(text(), "{section}")]'''
        option_locator = f"""{section_title}/ancestor::div[@class="styles__PictureNavigationWrapper-sc-7wjlys-0 jyKTUS"]
                        //span[contains(text(), "{option}")]"""
        element = self.find_element(section_title)
        if element:
            time.sleep(1)  # extra time to look like a human
            self.click(option_locator)

    def switch_to_iphone_page(self):
        explore_all_xpath = "//p[contains(., 'Explore all')]"
        stupid_frame = "//div[@id='slpespot']//iframe[@title='3rd party ad content']"
        self.driver.switch_to.frame(self.find_element(stupid_frame))
        self.find_element(explore_all_xpath).click()
        self.driver.switch_to.default_content()

    def get_item(self):
        time.sleep(1)
        item_xpath = (By.XPATH, '//div[@class="styles__StyledCol-sc-fw90uk-0 dOpyUp"]')
        self.wait.until(ec.presence_of_element_located(item_xpath))
        element = self.driver.find_elements(*item_xpath)
        return element

    def get_item_name(self, ancestor: str) -> str:
        name_xpath = f'{ancestor}//a[@data-test="product-title"]'
        element = self.find_element(name_xpath)
        return element.text

    def get_item_price(self, ancestor: str) -> str:
        price_xpath = f'{ancestor}//span[@data-test="current-price"]'
        element = self.find_element(price_xpath)
        return element.text

    def get_item_shipment(self, ancestor: str) -> str:
        shipment_xpath = f'{ancestor}//span[@data-test="LPFulfillmentSectionShippingFA_standardShippingMessage"]/span'
        try:
            element = WebDriverWait(self.driver, 1).until(ec.presence_of_element_located((By.XPATH, shipment_xpath)))
        except TimeoutException:
            return None
        else:
            return element.text

    def collect_items_data(self):
        collected_data = {}
        items_list = []
        items_list.extend(item for item in self.get_item())
        for i in range(1, len(items_list)+1):
            item_xpath = '//div[@class="styles__StyledCol-sc-fw90uk-0 dOpyUp"]'
            try:
                item_data = {
                    'name': self.get_item_name(f'{item_xpath}[{i}]'),
                    'price': self.get_item_price(f'{item_xpath}[{i}]'),
                    'shipment': self.get_item_shipment(f'{item_xpath}[{i}]')
                }
                collected_data[i] = item_data
            except NoSuchElementException as e:
                print(f'Error at XPath {item_xpath}[{i}]: {e}')
                continue
        return collected_data
