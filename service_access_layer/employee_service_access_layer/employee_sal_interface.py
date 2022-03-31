from abc import ABC, abstractmethod
from data_access_layer.employee_dao.employee_dao_interface import EmployeeDAOInterface
from entities.Employee import Employee


class EmployeeSALInterface(ABC):

    def __init__(self, employee_dao: EmployeeDAOInterface):
        self.employee_dao = employee_dao

    @abstractmethod
    def user_account_access(self, username: str, password: str) -> Employee:
        pass
