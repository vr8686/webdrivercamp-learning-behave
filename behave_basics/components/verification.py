def verify_element_contains(element_text: str, keyword: str):
    print(f'Checking if {element_text} contains word \"{keyword}\"...')
    if keyword in element_text.lower():
        print(f'Success. The element contains \"{keyword}\".')
    else:
        print(f'Mismatch. The element DOES NOT contain \"{keyword}\"')
