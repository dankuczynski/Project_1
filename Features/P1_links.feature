Feature: I want to access ticket reimbursement webpage

  Scenario: I want to login in ticket reimbursement page
   Given I am in the ticket reimbursement login page
   When I enter my username in the username field
   When I enter my password in the password field
   When I press the submit button
   Then I will be on ticket reimbursement home page

  Scenario: I want to create reimbursement ticket
    Given I am in the ticket reimbursement home page
    When I input the reimbursement reason in the reimbursement reason field
    When I input ticket reimbursement amount in the reimbursement amount field
    When I click on the submit button
    When I get create ticket success message
    Then I close create ticket success message

  Scenario: I want to view the reimbursement ticket
    Given I am in the ticket reimbursement home page
    When I press the view ticket button
    Then I can view the reimbursement ticket status

  Scenario: I want to delete the reimbursement ticket
    Given I am in the ticket reimbursement home page
    When I input a ticket number into the delete ticket field
    When I click the delete button
    When I will get a delete success message
    Then I close delete ticket success message

  Scenario: I want to logout from ticket reimbursement home page
    Given I am in the ticket reimbursement home page
    When I click on the logout button
    Then I redirect to login home page
