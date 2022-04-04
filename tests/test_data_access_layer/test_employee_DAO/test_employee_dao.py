from custom_exceptions.bad_employee_info import BadEmployeeInfo
from data_access_layer.employee_dao.employee_imp import EmployeeDAOImp

from entities.Employee import Employee

employee_dao = EmployeeDAOImp()


# def test_username_success():
#     result = employee_dao.reading_username("WillTest")
#     assert True


def test_read_employee_username_invalid_id():
    try:
        result = employee_dao.reading_username("papasmurf")
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Username was not found"


def test_read_employee_password_by_id():
    result = employee_dao.reading_password("D03sThisW0rk?")
    assert True


def test_read_employee_password_invalid_id():
    try:
        result = employee_dao.reading_password(2)
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Incorrect Employee information"
