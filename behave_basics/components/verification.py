def verify_price(collected_data: dict, condition: str):
    mismatches = []
    operators = {
        ">": lambda x, y: x > y,
        "<": lambda x, y: x < y
    }
    operator, value = condition.split()
    for item, item_data in collected_data.items():
        if item_data['price'] and '$' in item_data['price']:
            price = item_data['price'][item_data['price'].find('$') + 1:item_data['price'].find(' ', item_data['price'].find('$') + 1)]
            if operator in operators:
                if not operators[operator](float(price), int(value)):
                    mismatches.append((item_data['name'], item_data['price']))
            else:
                print("Operator has not been properly defined")
        else:
            print(f'Price for {item}. {item_data['name']} - cannot be seen.')
    if not mismatches:
        print('Prices of all the items meet expected condition')
    else:
        for item in mismatches:
            print(f'Price for {item[0]} - {item[1]} does not meet the condition - {condition}.')


def verify_shipping(collected_data: dict, condition: str):
    mismatches = []
    for item, item_data in collected_data.items():
        shipment_data = item_data.get('shipment')
        if shipment_data is None or condition not in shipment_data:
            mismatches.append((item_data['name'], item_data['shipment']))
    if not mismatches:
        print(f'Shipping conditions of all the items meet expected condition - {condition}')
    else:
        print(f"Items that do not meet expected shipment condition - {condition}:")
        for item in mismatches:
            print(f"- Item: {item[0]}, Shipment: {item[1]}")
