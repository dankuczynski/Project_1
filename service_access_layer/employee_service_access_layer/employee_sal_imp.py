from custom_exceptions.bad_employee_info import BadEmployeeInfo
from entities.Employee import Employee
from service_access_layer.employee_service_access_layer.employee_sal_interface import EmployeeSALInterface
from utils.manage_connection import connection


class EmployeeSALImp(EmployeeSALInterface):
    def user_account_access(self, username: str, password: str) -> Employee:
        sql = "select password from employee where username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        record = cursor.fetchone()
        if record is not None:
            employee = Employee(*record)
            return employee
        else:
            raise BadEmployeeInfo("Invalid employee information")

    def username_password_data_type_check(self, username: str, password: str):
        pass