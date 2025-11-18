Feature: Register on the utest.com website

    @TC-01
    Scenario: Fill in all the required fields for step 1
        Given I open de browser
        When  I navigate to "utest.com"
        And I click on the "Join Now" button
        Then I wait for the page "https://utest.com/signup/personal" to load
        When I fill the fields of the form
            | type   | field_name     | value              |
            | input  | First name:    | Ruben              |
            | input  | Last name:     | Smith              |
            | input  | Email address: | rsmith@example.com |
            | select | Month          | February           |
            | select | Day            | 5                  | 
            | select | Year           | 2000               |
        Then I valid that all fields have been filled correctly
        When I click on the "Next: Location" button
        Then I wait for the page "https://utest.com/signup/address" to load

