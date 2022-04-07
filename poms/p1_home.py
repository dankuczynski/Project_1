from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



class EmployeeReimbursement:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_alert(self):
        return self.driver.switch_to.alert

    def employee_username(self):
        element:  WebElement = self.driver.find_element(By.ID, "username")
        return element

    def employee_password(self):
        element:  WebElement = self.driver.find_element(By.ID, "password")
        return element

    def click_login(self):
        element: WebElement = self.driver.find_element(By.ID, "login")
        return element

    def create_reimbursement_ticket_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementReason")
        return element

    def create_reimbursement_ticket_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementTicketAmount")
        return element

    def click_create_reimbursement_ticket(self):
        element: WebElement = self.driver.find_element(By.ID, "create")
        return element

    def get_reimbursement_tickets(self):
        element: WebElement = self.driver.find_element(By.ID, "view")
        return element

    def delete_reimbursement_ticket(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteTicket")
        return element

    def delete_reimbursement_ticket_click(self):
        element: WebElement = self.driver.find_element(By.ID, "del")
        return element

    def employee_logout(self):
        element: WebElement = self.driver.find_element(By.ID, "log_out")
        return element


