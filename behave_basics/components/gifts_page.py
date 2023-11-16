from behave_basics.components.base import Base


class GiftsPage(Base):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def select_option_in_section(self, section, option):
        section_title = f'''//div[contains(@class, 'styles__PictureNavigationWrapper-sc-7wjlys-0 jyKTUS')]//h2//span[contains(@style, 'line-height:115%;display:block;')][contains(text(), "{section}")]'''
        option_locator = f"""{section_title}/ancestor::div[@class="styles__StyledGrid-sc-8k32oi-0 yMGkH"]//span[contains(text(), "{option}")]"""
        if self.find_element(section_title):
            self.click(option_locator)