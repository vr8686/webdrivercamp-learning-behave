  Feature: Target Gifts

  Background: User opens main page
    Given Navigate to https://www.target.com/

  Scenario: Navigate to the page
    When Search for gifts

  Scenario Outline: Verify searched page's headers
    When Search for <search_item>
    Then Verify header of the page contains <search_item>
    Examples:
      | search_item |
      | gift        |
      | iphone      |

  Scenario: Gifts - Price validation
    When Search for gifts
    When Select Her in Who’s on your list? section
    When Select Gifts under $15 in Gift ideas that fit your budget section
    Then Collect all items on the first page into collected_items on the feature level
    Then Verify all collected results' price is < 15
      | context.feature.collected_items |

  @no_background
  Scenario: Gift - Shipment validation
    Then Verify all collected results' shipment is Free shipping
      | context.feature.collected_items |