Feature: Automated Testing

Scenario: Register
      Given I go to homepage
	    When Clicking on the sign in button
	    Then I enter my email to register
	    Then I populate the registration form
      Then I click Submit
      Then Verify registration completed

    Scenario: Login
      Given I go to homepage
      When Clicking on the sign in button
      Then I enter my email to login
      Then Verify registration completed
