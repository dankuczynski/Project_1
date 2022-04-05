from custom_exceptions.bad_ticket_info import BadTicketInfo

from entities import Ticket
from service_access_layer.ticket_service_access_layer.ticket_sal_interface import TicketSALInterface


class TicketSALImp(TicketSALInterface):
    def cancel_ticket(self, ticket_number: int) -> bool:
        if type(ticket_number) != int:
            raise BadTicketInfo("Ticket number invalid")
        else:
            return True

    def create_ticket_sal(self, employee_id: int, reimbursement_reason: str, reimbursement_ticket_amount: float):
        if type(employee_id) != int:
            raise BadTicketInfo("Employee ID invalid")
        if type(reimbursement_reason) != str:
            raise BadTicketInfo("Reason type invalid")
        if type(reimbursement_ticket_amount) != float:
            raise BadTicketInfo("Amount value invalid")
        if len(reimbursement_reason) > 100:
            raise BadTicketInfo("Reason is too long")
        if reimbursement_ticket_amount > 1000.00:
            raise BadTicketInfo("Ticket amount invalid")
        if reimbursement_ticket_amount < 1:
            raise BadTicketInfo("Ticket amount invalid")
        return True

    def get_by_employee_id(self, employee_id: int) -> Ticket:
        if type(employee_id) != int:
            raise BadTicketInfo("")
        else:
            return Ticket

        # get list of ticket objects
        # make list to hold tickets as dictionaries
        # iterate through tickets, convert to dictionaries, store in dictionary list
        # send dictionary list to API for jsonify method

