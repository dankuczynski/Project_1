from custom_exceptions.bad_ticket_info import BadTicketInfo
from custom_exceptions.cancellation_fail import CancellationFail
from data_access_layer.ticket_dao.ticket_imp import TicketDAOImp
from entities.Ticket import Ticket
from service_access_layer.ticket_service_access_layer.ticket_sal_imp import TicketSALImp

ticket_dao = TicketDAOImp()
ticket_service = TicketSALImp(ticket_dao)
non_int_employee_id = Ticket(1, "Two", "I need ticket for food", 50.00)
non_str_reimbursement_reason = Ticket(1, 2, 1000, 50.00)
non_float_ticket_amount = Ticket(1, 2, "I need ticket for food", "Five")



def test_check_non_int_employee_id():
    try:
        ticket_service.create_ticket(non_int_employee_id)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Please pass valid employee Id"


def test_check_non_str_reimbursement_reason():
    try:
        ticket_service.create_ticket(non_str_reimbursement_reason)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Please pass valid reimbursement reason"


def test_check_reimbursement_reason_length():
    try:
        pass
    except:
        pass


def test_check_non_float_ticket_amount():
    try:
        ticket_service.create_ticket(non_float_ticket_amount)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Please pass valid ticket amount"


"""
def test_ticket_cancellation_success():
    try:
        ticket = Ticket(1, 20, "I need ticket for food", 50.00)
        ticket_service.cancel_ticket(1)
        assert True
    except CancellationFail as e:
        assert str(e) == "Fail to cancel ticket"


def test_ticket_cancellation_invalid_ticket_number():
    try:
        ticket = Ticket(0, 20, "I need ticket for food", 50.00)
        ticket_service.cancel_ticket(0)
        assert False
    except CancellationFail as e:
        assert str(e) == "Provided invalid ticket number"


def test_ticket_cancellation_invalid_employee_id():
    try:
        ticket = Ticket(1, 0, "I need ticket for food", 50.00)
        ticket_service.cancel_ticket(0)
        assert False
    except CancellationFail as e:
        assert str(e) == "Provided invalid Employee Id"


def test_ticket_cancellation_invalid_data_type_ticket_number():
    try:
        ticket = Ticket("A", 20, "I need ticket for food", 50.00)
        ticket_service.cancel_ticket(ticket.ticket_number)
        assert False
    except CancellationFail as e:
        assert str(e) == "Provided invalid ticket number"


def test_ticket_cancellation_invalid_data_type_employee_id():
    try:
        ticket = Ticket(1, "Two", "I need ticket for food", 50.00)
        ticket_service.cancel_ticket(ticket.employee_id)
        assert False
    except CancellationFail as e:
        assert str(e) == "Provided invalid Employee Id"  
        """""
