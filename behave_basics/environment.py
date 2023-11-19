from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from behave_basics.components.base import Base
from behave_basics.components.gifts_page import GiftsPage


def before_feature(context, feature):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.wait = WebDriverWait(context.browser, 10)
    context.base = Base(context.browser, context.wait)
    context.giftspage = GiftsPage(context.base.driver, context.base.wait)


def after_feature(context, feature):
    context.browser.quit()

def before_scenario(context, scenario):
    if '@no_background' in scenario.effective_tags:
        scenario.feature.background = None