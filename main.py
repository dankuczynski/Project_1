from werkzeug.utils import redirect

from custom_exceptions.bad_employee_info import BadEmployeeInfo
from utils.manage_connection import OperationalError, connect
import os

from entities.Ticket import Ticket
from data_access_layer.employee_dao.employee_imp import EmployeeDAOImp
from data_access_layer.ticket_dao.ticket_imp import TicketDAOImp
from service_access_layer.employee_service_access_layer.employee_sal_imp import EmployeeSALImp
from service_access_layer.ticket_service_access_layer.ticket_sal_imp import TicketSALImp


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app: Flask = Flask(__name__)
CORS(app) # use this to avoid cors errors

employee_dao = EmployeeDAOImp()
employee_service = EmployeeSALImp(employee_dao)

ticket_dao = TicketDAOImp()
ticket_service = TicketSALImp(ticket_dao)

# @app.get("/<name>")
# def get_greeting(name: str):
#     return jsonify({"message": f"Hello {name}"}), 200
#

@app.post("/body")
def sending_http_request_with_body():
        body: dict = request.get_json()
        employee_id = employee_dao.employee_id_username_password_match(body['1'], body['2'])
        employee_id_dictionary = {"employeeId" : employee_id}
        return jsonify(employee_id_dictionary), 200


@app.post("/create_and_view_tickets")
def making_tickets():
    body: dict = request.get_json()
    ticket_num = ticket_dao.create_ticket(body["1"], body["2"], body["3"])
    view_single_ticket = ticket_dao.get_ticket_by_ticket_number(ticket_num)
    ticket_dict = view_single_ticket.ticket_dictionary_conversion()
    return jsonify(ticket_dict), 200
    # Ticket_Dict= Ticket_num.ticket_number_dictionary_conversion()
    # return jsonify(Ticket_Dict), 200

@app.get("/create_and_view_tickets")
def viewing_tickets():
    body: dict = request.get_json



app.run()