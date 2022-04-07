from behave import given, when, then
from selenium.webdriver.support.expected_conditions import alert_is_present, title_contains
from selenium.webdriver.support.wait import WebDriverWait

# @given(u'I am in the ticket reimbursement login page')
# def step_impl(context):
#    context.driver.get(C:/Users/Almas/Desktop/Project_1/api/login.html)

@given(u'I am in the ticket reimbursement login page')
def step_impl(context):
    context.driver.get("C:/Python/Project_1/api/login.html")


@when(u'I enter my {username} in the username field')
def step_impl(context, username):
    context.p1_home.employee_username().send_keys(username)


@when(u'I enter my {password} in the password field')
def step_impl(context, password):
    context.p1_home.employee_password().send_keys(password)


@when(u'I press the submit button')
def step_impl(context):
    context.p1_home.click_login().click()


@then(u'I will be on {titley} page')
def step_impl(context, titley: str):
    WebDriverWait(context.driver, 1).until(title_contains(titley))
    assert context.driver.title == titley
    # assert context.driver.get("create_and_view_tickets")


@given(u'I am in the ticket reimbursement home page')
def step_impl(context):
    #context.driver.get(C:/Users/Almas/Desktop/Project_1/api/login.html)
    context.driver.get("C:/Python/Project_1/api/login.html")
    WebDriverWait(context.driver, 1).until(title_contains("Login"))
    context.p1_home.employee_username().send_keys("WillTest")
    context.p1_home.employee_password().send_keys("D03sThisW0rk?")
    context.p1_home.click_login().click()

@given(u'I am in the ticket reimbursement home page a')
def step_impl(context):
    context.driver.get("C:/Python/Project_1/api/tickets.html")

@when(u'I click on the submit button')
def step_impl(context):
    context.p1_home.click_create_reimbursement_ticket().click()


@when(u'I get create ticket success message')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())



@then(u'I close create ticket success message')
def step_impl(context):
    context.p1_home.get_alert().accept()


@when(u'I press the view ticket button')
def step_impl(context):
    context.p1_home.get_reimbursement_tickets().click()



@then(u'I can view the reimbursement ticket status')
def step_impl(context):
    WebDriverWait(context.driver, 4)


@when(u'I input a {ticketNumber} into the delete ticket field')
def step_impl(context, ticketNumber):
    context.p1_home.delete_reimbursement_ticket().send_keys(ticketNumber)


@when(u'I click the delete button')
def step_impl(context):
    context.p1_home.delete_reimbursement_ticket_click().click()


@when(u'I will get a delete success message')
def step_impl(context):
    WebDriverWait(context.driver, 4).until(alert_is_present())


@then(u'I close delete ticket success message')
def step_impl(context):
    context.p1_home.get_alert().accept()

@when(u'I click on the logout button')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("create_and_view_tickets"))
    context.p1_home.employee_logout().click()


@then(u'I redirect to login home page')
def step_impl(context):
    assert context.driver.title == "Login"

@when(u'I input {reimbursementReason} in the reimbursement reason field')
def step_impl(context, reimbursementReason: str):
    context.p1_home.create_reimbursement_ticket_reason().send_keys(reimbursementReason)

@when(u'I input ticket {reimbursementAmount} in the reimbursement amount field')
def step_impl(context, reimbursementAmount: float):
    context.p1_home.create_reimbursement_ticket_amount().send_keys(reimbursementAmount)