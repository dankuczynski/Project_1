from custom_exceptions.bad_ticket_info import BadTicketInfo
from service_access_layer.ticket_service_access_layer.ticket_sal_interface import TicketSALInterface
from utils.manage_connection import connection


class TicketSALImp(TicketSALInterface):
    def cancel_ticket(self, ticket_number: int) -> bool:
        sql = "truncate * from ticket where ticket_number = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [ticket_number])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise BadTicketInfo("No ticket found with that ticket number")
