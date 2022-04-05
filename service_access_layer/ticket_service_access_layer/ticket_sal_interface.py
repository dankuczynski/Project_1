from abc import ABC, abstractmethod
from data_access_layer.ticket_dao.ticket_interface import TicketDAOInterface
from entities.Ticket import Ticket


class TicketSALInterface(ABC):

    def __init__(self, ticket_dao):
        self.ticket_dao: TicketDAOInterface = ticket_dao

    @abstractmethod
    def cancel_ticket(self, tick_number: int) -> bool:
        pass

    @abstractmethod
    def create_ticket_sal(self, employee_id: int, reimbursement_reason: str, reimbursement_ticket_amount: float):
        pass

    @abstractmethod
    def get_by_employee_id(self, ticket: Ticket):
        pass
