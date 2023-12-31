import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from behave_basics.components.base import Base


class GiftsPage(Base):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def select_option_in_section(self, section, option):
        section_title = f'//h2//span[contains(text(), "{section}")]'
        option_locator = (f'{section_title}/ancestor::div[@class="styles__PictureNavigationWrapper-sc-7wjlys-0 jyKTUS"]'
                          f'//span[contains(text(), "{option}")]')
        element = self.find_element(section_title)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element:
            time.sleep(1)  # extra time to look like a human
            self.click(option_locator)

    def switch_to_iphone_page(self):
        explore_all_xpath = "//p[contains(., 'Explore all')]"
        frame = "//div[@id='slpespot']//iframe[@title='3rd party ad content']"
        self.driver.switch_to.frame(self.find_element(frame))
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
            element = self.find_present_element(shipment_xpath)
        except TimeoutException:
            return None
        else:
            return element.text

    def collect_items_data(self):
        collected_data = {}
        items_list = []
        items_list.extend(item for item in self.get_item())
        for i in range(1, len(items_list) + 1):
            item_xpath = f'//div[@class="styles__StyledCol-sc-fw90uk-0 dOpyUp"][{i}]'
            try:
                element = self.find_element(item_xpath)
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(0.5)
                item_data = {
                    'name': self.get_item_name(item_xpath),
                    'price': self.get_item_price(item_xpath),
                    'shipment': self.get_item_shipment(item_xpath)
                }
                collected_data[i] = item_data
            except NoSuchElementException:
                print(f'Error at XPath {item_xpath} - no such element')
                continue
            except TimeoutException:
                print(f'Error at XPath {item_xpath} - TimeoutException')
                continue
            except StaleElementReferenceException:
                print(f'Error at XPath {item_xpath} - stale element not found')
        return collected_data
