from custom_exceptions.bad_ticket_info import BadTicketInfo
from custom_exceptions.cancellation_fail import CancellationFail
from data_access_layer.ticket_dao.ticket_imp import TicketDAOImp
from entities.Ticket import Ticket
from service_access_layer.ticket_service_access_layer.ticket_sal_imp import TicketSALImp

ticket_dao = TicketDAOImp()
ticket_service = TicketSALImp(ticket_dao)


def test_check_non_int_employee_id():
    try:
        ticket_service.create_ticket_sal("Two", "I need ticket for food", 50.00)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Employee ID invalid"


def test_check_non_str_reimbursement_reason():
    try:
        ticket_service.create_ticket_sal(2, 1000, 50.00)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Reason type invalid"


def test_check_non_float_ticket_amount():
    try:
        ticket_service.create_ticket_sal(2, "I need ticket for food", "Five")
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Amount value invalid"


def test_check_reimbursement_reason_length():
    try:
        ticket_service.create_ticket_sal(2,
                                         "I need ticket for food!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                                         50.00)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Reason is too long"


def test_check_ticket_amount_over_limit():
    try:
        ticket_service.create_ticket_sal(2, "I need ticket for food", 2500.00)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Ticket amount invalid"


def test_check_ticket_amount_under_limit():
    try:
        ticket_service.create_ticket_sal(2, "I need ticket for food", -1.00)
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Ticket amount invalid"


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
