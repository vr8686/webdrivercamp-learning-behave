from behave_basics.components.base import Base
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
            self.click(option_locator)
            self.wait.until(ec.visibility_of_element_located((By.XPATH, self.PRODUCTLIST)))

    def switch_to_iphone_page(self):
        explore_all_xpath = "//p[contains(., 'Explore all')]"
        stupid_frame = "//div[@id='slpespot']//iframe[@title='3rd party ad content']"
        self.driver.switch_to.frame(self.find_element(stupid_frame))
        self.find_element(explore_all_xpath).click()
        self.driver.switch_to.default_content()

    def get_item(self):
        item_xpath = (By.XPATH, self.ITEM_XPATH)
        self.wait.until(ec.presence_of_element_located(item_xpath))
        element = self.driver.find_elements(*item_xpath)
        return element

    def get_item_name(self, number):
        name_xpath = f'({self.ITEM_NAME_XPATH})[{number}]'
        element = self.find_element(name_xpath)
        return element

    def get_item_price(self, number):
        price_xpath = f'({self.ITEM_PRICE_XPATH})[{number}]'
        element = self.find_element(price_xpath)
        return element

    def collect_items_data(self):
        collected_data = {}
        items_list = []
        items_list.extend(item for item in self.get_item())
        for i in range(1, len(items_list)+1):
            item_data = {'name': self.get_item_name(i).text, 'price': self.get_item_price(i).text}
            collected_data[i] = item_data
        print(len(items_list))
        # print(collected_data)
        return collected_data
