from custom_exceptions.bad_employee_info import BadEmployeeInfo
from custom_exceptions.bad_ticket_info import BadTicketInfo
from data_access_layer.ticket_dao.ticket_imp import TicketDAOImp
from entities.Ticket import Ticket

ticket_dao = TicketDAOImp()


def test_create_ticket_success():
    result = ticket_dao.create_ticket(1, "reimbursement_reason", 500.00)
    assert result


def test_create_ticket_invalid_reimbursement_reason():
    try:
        result = ticket_dao.create_ticket(1, 100, 500.00)
        assert result != int
    except BadTicketInfo as e:
        assert str(e) == "Incorrect ticket information"


def test_create_ticket_empty_string():
    try:
        result = ticket_dao.create_ticket(1, "", 500.00)
        assert result != ""
    except BadTicketInfo as e:
        assert str(e) == "Incorrect ticket information"


def test_create_ticket_excess_amount():
    try:
        result = ticket_dao.create_ticket(1, "travel", 2000.00)
        assert result <= 1000.00
    except BadTicketInfo as e:
        assert str(e) == "Incorrect ticket information"


def test_create_ticket_equal_less_than_zero_amount():
    try:
        result = ticket_dao.create_ticket(1, "transport", 0)
        assert result > 0
    except BadTicketInfo as e:
        assert str(e) == "Incorrect ticket information"


# def test_create_ticket_reason_length():
#     try:
#         result = ticket_dao.create_ticket(1,
#                         "Travel ticket from washington to boston asdlkfjsdajlk;fjasdlkf;jsaed;flkasj df ;lkasejdf;laskdjf;lsadixjfsdal;kjfsadfasedfsdfasdflkjasd;lkfjwaeolkjras;lkdjf;sdlkfja;lsdkjf;sdalkjf;asldkjfas;ldkjf",
#                         500.00)
#         assert result <= 100
#     except BadTicketInfo as e:
#         assert str(e) == "too long ticket information"


def test_get_all_ticket_by_employee_id():
    result = ticket_dao.get_all_ticket_by_employee_id(1)
    assert len(result) >= 1

def test_delete_ticket_success():
    result = ticket_dao.delete_ticket(0)
    assert result


def test_delete_ticket_invalid_data_type():
    try:
        result = ticket_dao.delete_ticket("two")
        assert False
    except BadTicketInfo as e:
        assert str(e) == "Incorrect Ticket information"


def test_delete_ticket_invalid_ticket_number():
    try:
        result = ticket_dao.delete_ticket(-1)
        assert result != str
    except BadTicketInfo as e:
        assert str(e) == "Incorrect ticket information"
