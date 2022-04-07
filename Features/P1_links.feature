Feature: I want to access ticket reimbursement webpage

  Scenario Outline: I want to login in ticket reimbursement page
   Given I am in the ticket reimbursement login page
   When I enter my <username> in the username field
   When I enter my <password> in the password field
   When I press the submit button
   Then I will be on <titley> page

        Examples:
          | username | password     | reimbursementReason | reimbursementAmount | ticketNumber | titley                  |
          | KefkaW0n | C1dh4sN0Sh1p | I need money        | 500.00              | 6            | create_and_view_tickets |

  Scenario Outline: I want to create reimbursement ticket
    Given I am in the ticket reimbursement home page
    When I input the <reimbursementReason> in the reimbursement reason field
    When I input ticket <reimbursementAmount> in the reimbursement amount field
    When I click on the submit button
    When I get create ticket success message
    Then I close create ticket success message

        Examples:
          | username | password      | reimbursementReason | reimbursementAmount | ticketNumber |
          | WillTest | D03sThisW0rk? | food                | 15.00               | 6            |

  Scenario: I want to view the reimbursement ticket
    Given I am in the ticket reimbursement home page
    When I press the view ticket button
    Then I can view the reimbursement ticket status

  Scenario Outline: I want to delete the reimbursement ticket
    Given I am in the ticket reimbursement home page
    When I input a <ticketNumber> into the delete ticket field
    When I click the delete button
    When I will get a delete success message
    Then I close delete ticket success message

        Examples:
          | username | password      | reimbursementReason | reimbursementAmount | ticketNumber |
          | WillTest | D03sThisW0rk? | I need money        | 500.00              | 6            |

  Scenario: I want to logout from ticket reimbursement home page
    Given I am in the ticket reimbursement home page a
    When I click on the logout button
    Then I redirect to login home page