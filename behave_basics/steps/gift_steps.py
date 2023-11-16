from behave import *


@step('Navigate to {url}')
def step_impl(context, url):
    context.browser.get(url)


@when("Search for {search_item}")
def step_impl(context, search_item):
    context.base.search_for_item(search_item)


@then("Verify header of the page contains {search_item}")
def step_impl(context, search_item):
    context.base.verify_element_contains(context.h1header, search_item)


@when("Select {option} in {section} section")
def step_impl(context, option, section):
    context.giftspage.select_option_in_section(section, option)
