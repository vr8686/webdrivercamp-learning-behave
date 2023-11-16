from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from behave_basics.components.base import Base
from behave_basics.components.gifts_page import GiftsPage


def before_all(context):
    context.browser = webdriver.Chrome()
    context.wait = WebDriverWait(context.browser, 10)
    context.base = Base(context.browser, context.wait)
    context.giftspage = GiftsPage(context.base.driver, context.base.wait)
    context.h1header = context.base.H1HEADER

def after_all(context):
    context.browser.quit()
