### User Stories

    - As an employee, I should be able to log in.
        Given: Employee is on Employee Login page
        When: Employee pushes log in button
        When: Employee enters username
        When: Employee enters password
        When: Employee pressed submit
        Then: Employee directed to Account Page

    - As an employee, I should be able to log out.
        Given: Employee is on Account Page
        When: Employee pressed log out button
        When: Employee presses confirm
        Then: Employee directed to Employee Login page

    - As an employee, I should be able to create a ticket.
        Give: Employee is on Account page
        When: Employee pressed create ticket button
        When: Employee directed to Ticket creation screen
        When: Employee enters ticket reason
        When: Employee enters reinbursement amount
        When: Employee presses submit
        When: Employee enters username
        When: Employee enters password
        Then: Employee has submitted ticket

    - As an employee, I should be able to cancel a ticket.
        Give: Employee is on Account page
        When: Employee selects pending ticket
        When: Employee selects cancel ticket
        When: Employee enters username
        When: Employee enters password
        Then: Employee cancels ticket

    - As an employee, I should be able to see ticket(s) status.
        Give: Employee is on Account page
        Then: Employee can see all reinbursement requests

    - As an employee, I should be given notice upon successful request.
        Given: Employee creates ticket
        When: Ticket passes all checks
        Then: Employee shown sucessful create message

    - As an employee, I should be given notice upon failed request.
        Given: Employee creates ticket
        When: Ticket fails any check
        Then: Employee show failed create message
