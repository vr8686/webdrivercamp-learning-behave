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
    context.base.verify_header_contains(search_item)


@when("Select {option} in {section} section")
def select_option_in_section(context, option, section):
    context.giftspage.select_option_in_section(section, option)


@then("Collect all items on the first page into {var} on the {level} level")
def step_impl(context, var, level=None):
    items = context.giftspage.collect_items_data()
    if level is not None:
        setattr(context.feature, var, items)
    else:
        setattr(context, var, items)
    # for item, item_data in context.feature.collected_items.items():
    #     print(f"{item_data['name']} - {item_data['price']}, {item_data['shipment']}")

@step('Verify all collected results\' {param} is {condition}')
def step_impl(context, param, condition):
    parameters = {"price": context.verification.verify_price,
                  "shipment": context.verification.verify_shipping}
    if param in parameters:
        parameters[param](context.feature.collected_items, condition)
    else:
        print(f'Wrong \'param\' - {param}')
