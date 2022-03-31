from data_access_layer.ticket_dao.ticket_dao_imp import TicketDAOImp
from custom_exceptions.bad_ticket_info import BadTicketInfo
from entities.Ticket import Ticket
import pytest

ticket_dao = TicketDAOImp()

def test_create_ticket_success():
    try:
        ticket = Ticket(1, 1, "I need money", 500.00)
        result = ticket_dao.create_ticket(ticket)
        assert result.ticket_number != 0
    except BadTicketInfo as e:
        raise str(e) == "Incorrect ticket information"

def create_ticket_invalid_datatype():
    try:
        result = ticket_dao.create_ticket(0)
        assert result.ticket_number != 0
    except BadTicketInfo as e:
        raise str(e) == "Incorrect ticket information"