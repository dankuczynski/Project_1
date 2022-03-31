from abc import ABC, abstractmethod
from data_access_layer.ticket_dao.ticket_interface import TicketDAOInterface
from entities.Ticket import Ticket


class TicketSALInterface(ABC):

    def __init__(self, ticket_dao):
        self.ticket_dao : TicketDAOInterface = ticket_dao

    @abstractmethod
    def cancel_ticket(self, tick_number: int) -> Ticket:
        pass

