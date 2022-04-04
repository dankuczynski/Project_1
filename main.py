from werkzeug.utils import redirect
from custom_exceptions.bad_employee_info import BadEmployeeInfo
from utils.manage_connection import OperationalError, connect
import os

from entities.Ticket import Ticket
from data_access_layer.employee_dao.employee_imp import EmployeeDAOImp
from data_access_layer.ticket_dao.ticket_imp import TicketDAOImp
from service_access_layer.employee_service_access_layer.employee_sal_imp import EmployeeSALImp
from service_access_layer.ticket_service_access_layer.ticket_sal_imp import TicketSALImp
from custom_exceptions.bad_ticket_info import BadTicketInfo

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app: Flask = Flask(__name__)
CORS(app) # use this to avoid cors errors

employee_dao = EmployeeDAOImp()
employee_service = EmployeeSALImp(employee_dao)

ticket_dao = TicketDAOImp()
ticket_service = TicketSALImp(ticket_dao)

@app.post("/body")
def sending_http_request_with_body():
    try:
        body: dict = request.get_json()
        employee_id = employee_dao.employee_id_username_password_match(body['1'], body['2'])
        employee_id_dictionary = {"employeeId" : employee_id}
        return jsonify(employee_id_dictionary), 200
    except BadEmployeeInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400

@app.post("/tickets")
def making_tickets():
   # try block
   # accept data access layer connection problem, create a json
   # return that ConnectionProblem as json
    try:
        body: dict = request.get_json()
        # print(body)
        # return jsonify(body)
        print(body)
        ticket_num = ticket_dao.create_ticket(int(body["1"]), body["2"], float(body["3"]))
        ticket_num_dictionary = {"ticketNumber": ticket_num}
        return jsonify(ticket_num_dictionary)
    except BadEmployeeInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.get("/tickets/<employeeId>")
def viewing_tickets(employeeId: str):
    try:
        tickets = ticket_dao.get_all_ticket_by_employee_id(int(employeeId))
        # print(tickets)
        tickets = jsonify(tickets)
        return tickets, 200
    except BadEmployeeInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    # service layer to handle conversion
    # service layer to turn into Ticket objects into dictionaries
    # list of dictionaries and jsonify them
    # return jsonified dictionary, 200

    #service access layer to validate it


@app.delete("/tickets/delete/<ticket_num>")
def deleting_ticket(ticket_num: str):
    try:
        ticket_dao.delete_ticket(int(ticket_num))
        return "deletion successful!"
    except BadTicketInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()