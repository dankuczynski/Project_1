from custom_exceptions.bad_ticket_info import BadTicketInfo

from entities import Ticket
from service_access_layer.ticket_service_access_layer.ticket_sal_interface import TicketSALInterface
from utils.manage_connection import connection


class TicketSALImp(TicketSALInterface):
    def cancel_ticket(self, ticket_number: int) -> bool:
        sql = "delete * from ticket where ticket_number = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [ticket_number])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise BadTicketInfo("No ticket found with that ticket number")

    def create_ticket(self, ticket: Ticket) -> Ticket:
        if type(ticket.ticket_number) != int:
            raise BadTicketInfo("Ticket number invalid")
        if type(ticket.employee_id) != int:
            raise BadTicketInfo("Employee ID invalid")
        if type(ticket.reimbursement_reason) != str:
            raise BadTicketInfo("Reason type invalid")
        if type(ticket.reimbursement_ticket_amount) != float:
            raise BadTicketInfo("Amount value invalid")
        if len(ticket.reimbursement_reason) > 100:
            raise BadTicketInfo("Reason is too long")
        if ticket.reimbursement_ticket_amount > 1000.00:
            raise BadTicketInfo("Ticket amount invalid")
        