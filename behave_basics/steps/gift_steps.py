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


@then("Collect all items on the first page into {context_var} on the {level} level")
def step_impl(context, context_var, level=None):
    items = context.giftspage.collect_items_data()
    if level:
        setattr(context.feature, context_var, items)
    else:
        setattr(context, context_var, items)
    for item, item_data in context.feature.collected_items.items():
        print(f"{item_data['name']} - {item_data['price']}, {item_data['shipping']}")


@step('Verify all collected results\' {param} is {condition}')
def step_impl(context, param, condition):
    for item, item_data in context.feature.collected_items.items():
        if item_data['price']:
            price = item_data['price']
            price_cleaned = price[price.find('$') + 1:price.find(' ', price.find('$') + 1)]
            print(f"OK. Price of {item_data['name'][:20]} is ${price_cleaned} and < 15"
                  if context.giftspage.verify_price(price_cleaned)
                  else f"MISMATCH. Price of {item_data['name'][:20]} is ${price_cleaned} and higher than 15")

