from custom_exceptions.bad_employee_info import BadEmployeeInfo
from data_access_layer.employee_dao.employee_imp import EmployeeDAOImp
from service_access_layer.employee_service_access_layer.employee_sal_imp import EmployeeSALImp

employee_dao = EmployeeDAOImp()
employee_service = EmployeeSALImp(employee_dao)

"""
Create service tests
"""

"""def test_user_login_success():
    result = employee_service.user_account_access("WillTest", "Do3sThisW0rk?")
    assert result """


def test_invalid_user_name_success():
    try:
        employee_service.user_account_access("WillTest ", "Do3sThisW0rk?")
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Invalid employee information"


def test_invalid_password_length():
    try:
        employee_service.user_account_access("WillTest ",
                                             "Do3sThisW0rk?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Invalid employee information"


def test_invalid_username_length():
    try:
        employee_service.user_account_access("WillTest!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                                             "Do3sThisW0rk?")
        assert False
    except BadEmployeeInfo as e:
        assert str(e) == "Invalid employee information"
