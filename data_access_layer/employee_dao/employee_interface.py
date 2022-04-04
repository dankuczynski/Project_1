from abc import ABC, abstractmethod

from entities.Employee import Employee


class EmployeeDAOInterface(ABC):

    @abstractmethod
    def reading_username(self, username: str) -> Employee:
        pass

    @abstractmethod
    def reading_password(self, password: str) -> Employee:
        pass

    @abstractmethod
    def employee_id_username_password_match(self, username: str, password: str) -> int:
        pass