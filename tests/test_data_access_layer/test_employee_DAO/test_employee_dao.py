from custom_exceptions.bad_employee_info import BadEmployeeInfo
from data_access_layer.employee_dao.employee_imp import EmployeeDAOImp

from entities.Employee import Employee

employee_dao = EmployeeDAOImp()


def test_read_employee_username_by_id():
    employee = Employee(1, username: str, password: str)
    result = employee_dao.read_employee_username_by_id()
    assert True


def test_read_employee_username_invalid_id():
    try:
        employee = Employee(1, username: str, password: str)
        result = employee_dao.get_employee_username_by_id()
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Incorrect Employee information"


def test_read_employee_password_by_id():
    employee = Employee(1, username: str, password: str)
    result = employee_dao.reading_password()
    assert True


def test_read_employee_password_invalid_id():
    try:
        employee = Employee(1, username: str, password: str)
        result = employee_dao.read_employee_password_by_id()
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Incorrect Employee information"
