from behave import *


@step('Print the current url')
def print_current_url(context):
    print(context.browser.current_url)


@step('Navigate to {url}')
def navigate_to_url(context, url):
    context.browser.get(url)
    print_current_url(context)


@when("Search for {search_item}")
def search_for_item(context, search_item):
    context.base.search_for_item(search_item)


@step("Verify header of the page contains {search_item}")
def verify_header_contains(context, search_item):
    if search_item == 'iphone':
        context.giftspage.switch_to_iphone_page()
    context.base.verify_header_contains(search_item)


@step("Select {option} in {section} section")
def select_option_in_section(context, option, section):
    context.giftspage.select_option_in_section(section, option)


# @step("Collect all items on the first page into {var}")
# def step_impl(context, var):
#     items = context.giftspage.collect_items_data()
#     setattr(context, var, items)


@step("Collect all items on the first page into {var} on the {level} level")
def step_impl(context, var, level=None):
    items = context.giftspage.collect_items_data()
    context_levels = {
        "scenario": context,
        "feature": context.feature,
        None: context
    }
    context_level = context_levels.get(level, None)
    if context_level is None:
        print("Invalid context level")
        raise ValueError
    setattr(context_level, var, items)
    print(f'Collected data for {len(getattr(context_level, var))} items')


@step('Verify all collected results\' {param} is {condition}')
def step_impl(context, param, condition):
    collected_items = eval(context.table.headings[0])
    parameters = {"price": context.verification.verify_price,
                  "shipment": context.verification.verify_shipping}
    if param in parameters:
        parameters[param](collected_items, condition)
    else:
        print(f'Wrong \'param\' - {param}')
