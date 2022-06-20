Feature: navigate

  In order to test the newly built website
  As a programmer
  I need to register a new user

  @Test_Register
  Scenario: Navigate to the Register page
    Given I am at the home page
    When I press the Register button
    Then I should see the register form
