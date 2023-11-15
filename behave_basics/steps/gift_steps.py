from behave import *
from behave_basics.components import verification
import time


@step('Navigate to {url}')
def step_impl(context, url):
    context.browser.get(url)


@when("Search for {search_item}")
def step_impl(context, search_item):
    context.base.type_and_send_return(context.SEARCHBAR, search_item)
    time.sleep(3)


@then("Verify header of the page contains {search_item}")
def step_impl(context, search_item):
    context.header_text = context.base.get_text(context.H1HEADER)
    verification.verify_element_contains(context.header_text, search_item)