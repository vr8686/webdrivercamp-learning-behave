from behave import *


@step('Navigate to {url}')
def navigate_to_url(context, url):
    context.browser.get(url)


@when("Search for {search_item}")
def search_for_item(context, search_item):
    context.base.search_for_item(search_item)


@then("Verify header of the page contains {search_item}")
def verify_header_contains(context, search_item):
    if search_item == 'iphone':
        context.giftspage.switch_to_iphone_page()
    context.base.verify_element_contains(context.h1header, search_item)


@when("Select {option} in {section} section")
def select_option_in_section(context, option, section):
    context.giftspage.select_option_in_section(section, option)


@then("Collect all items on the first page into {context_var}")
def step_impl(context, context_var):
    items = context.giftspage.collect_items_data()
    setattr(context, context_var, items)
    for item in getattr(context, context_var).keys():
        print(f"{getattr(context, context_var)[item]['name']} - {getattr(context, context_var)[item]['price']}")
