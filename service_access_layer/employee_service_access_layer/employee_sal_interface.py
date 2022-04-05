from abc import ABC, abstractmethod
from data_access_layer.employee_dao.employee_interface import EmployeeDAOInterface
from entities.Employee import Employee


class EmployeeSALInterface(ABC):

    def __init__(self, employee_dao):
        self.employee_dao : EmployeeDAOInterface = employee_dao

    @abstractmethod
    def user_account_access(self, username: str, password: str) -> Employee:
        pass

    @abstractmethod
    def username_password_data_type_check(self, username: str, password: str):
        pass
