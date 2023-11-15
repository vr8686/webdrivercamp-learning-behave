from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from behave_basics.components.base import Base
from behave_basics.components import verification


def before_all(context):
    context.browser = webdriver.Chrome()
    context.wait = WebDriverWait(context.browser, 10)
    context.base = Base(context.browser, context.wait)
    context.verification = verification
    context.SEARCHBAR = ('//div[@class="styles__SearchWrapper-sc-1ywf0d0-0 bpBcjs"]'
                         '//input[contains(@placeholder, "What can we help you find?")]')
    context.H1HEADER = '//h1[@data-test="page-title"]'

def after_all(context):
    context.browser.quit()