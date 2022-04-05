from abc import ABC, abstractmethod


class TicketDAOInterface(ABC):

    @abstractmethod
    def create_ticket(self, employee_id, reimbursement_reason, reimbursement_ticket_amount):
        pass

    @abstractmethod
    def get_all_ticket_by_employee_id(self, employee_id: int):
        pass

    @abstractmethod
    def delete_ticket(self, ticket_number: int):
        pass
