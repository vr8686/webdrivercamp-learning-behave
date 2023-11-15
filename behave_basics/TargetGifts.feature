Feature: Target Gifts

  Scenario: Navigate to the page
    Given Navigate to https://www.target.com/
    When Search for gifts



  Scenario Outline: Verify searched page's headers
    Given Navigate to https://www.target.com/
    When Search for <search_item>
    Then Verify header of the page contains <search_item>
    Examples:
      | search_item |
      | gift        |
      | iphone      |