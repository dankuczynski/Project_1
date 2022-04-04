from custom_exceptions.bad_employee_info import BadEmployeeInfo
from data_access_layer.employee_dao.employee_interface import EmployeeDAOInterface
from entities.Employee import Employee
from utils.manage_connection import connection


class EmployeeDAOImp(EmployeeDAOInterface):

    def reading_username(self, username: str) -> Employee:
        sql = "select * from employee where username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        record = cursor.fetchone()
        if record is not None:
            employee = Employee(*record)
           # employee = Employee(1, "WillTest", "D03sThisW0rk?")
            return employee
        else:
            raise BadEmployeeInfo("Username was not found")

    def reading_password(self, password: str) -> Employee:
        sql = "select * from employee where password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [password])
        record = cursor.fetchone()
        if len(record) != 0:
            employee = Employee(*record)
            return employee
        else:
            raise BadEmployeeInfo("Password does not match.")

    def employee_id_username_password_match(self, username: str, password: str) -> int:
        sql = "select employee_id from employee where username = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [username, password])
        record = cursor.fetchone()
        if len(record) != 0:
            employee_id = record[0]
            return employee_id
        else:
            raise BadEmployeeInfo("Username and Password do not match")