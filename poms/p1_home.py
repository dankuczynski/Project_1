from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class EmployeeReimbursement:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def employee_login(self):
        element: WebElement = self.driver.find_element(By.ID, "name")
        return element

    def create_reimbursement_ticket(self):
        return self.driver.find_element(By.ID, "searchInput")

    def get_reimbursement_ticket(self):
        pass

    def delete_reimbursement_ticket(self):
        pass

    def employee_logout(self):
        pass
