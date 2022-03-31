from custom_exceptions.bad_employee_info import BadEmployeeInfo
from data_access_layer.employee_dao.employee_imp import EmployeeDAOImp
from entities.Employee import Employee

employee_dao = EmployeeDAOImp()


def test_read_employee_username_by_id():
    employee = Employee()
    result = employee_dao.reading_username(employee)
    assert True


def test_read_employee_username_invalid_id():
    try:
        employee = Employee()
        result = employee_dao.reading_username(employee)
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Incorrect Employee information"


def test_read_employee_password_by_id():
    employee = Employee()
    result = employee_dao.reading_password(employee)
    assert True


def test_read_employee_password_invalid_id():
    try:
        employee = Employee()
        result = employee_dao.reading_password(employee)
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Incorrect Employee information"
