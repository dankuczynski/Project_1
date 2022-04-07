from selenium import webdriver
from behave.runner import Context
from poms.p1_home import EmployeeReimbursement


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.p1_home = EmployeeReimbursement(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
