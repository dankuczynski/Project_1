# Test Strategy


### Best Practices:
- use CRUD ope
- Start off with the interface
- Use proper naming conventions, no abbreviations: long form names in snake_case
- Push to git a lot
- 

### API Endpoints:

- JSON formatting
- Uploading to database and downloading from
- Nesting (http://localhost:5000/Customer , http://localhost:5000/Customer/Delete)


### Bug Reporting:

- Excel/Google sheets
- List where (what line) the bug is, and the directory, name, method/function/test
- Update spreadsheet when bug is finished

# Test Plan



### Technology

- Python
- Pycharm
- Flask
- DBeaver-Postgres
- Pytest
- AWS RDS
- Psycopg[binary]
- EC2
- Github/Git
- Gitbash
- Postman
- Google Draw


### Scope

- Entities:
    - Employee(
        employee_id int Primary Key,
        username varchar(20),
        password varchar(20)
    );


    - Ticket(
        ticket_number serial primary key,
        ticket_status varchar(10),
        employee_id int foreign key,        
        reimbursement_reason varchar(100),
        reimbursement_ticket_amount float

    );

- Testing plan

    - Data_Access_Layer
        
        - C:
        - Positive 
            - create_ticket_success()
        - Negative
            - create_ticket_invalid_datatype()
            - create_ticket_empty_string()
            - create_tickeet_invalid_employee_id()
            - create_ticket_excess_amount()
            - create_ticket_zero_and_less_than_zero()
            - create_ticket_reason_length()
            - create_ticket_reason_invalid_datatype()
            - create_ticket_reason_invalid_empty_string()


        - R:
        - Positive
            - get_ticket_status_sucess()
            - get_all_ticket_by_employee_id_success()
        - Negative
            - get_ticket_status_invalid_ticket_number()
            - get_ticket_status_invalid_data_type()
            - get_all_tickets_invalid_employee_id()
            - get_all_tickets_invalid_datatype()


        - U:
        - Positive
            - update_ticket_success()
        - Negative
            - update_ticket_invalid_ticket_number()
            - update_ticket_invalid_data_type()


        - D:
        - Postitive
            - delete_ticket_success()
        - Negative
            - delete_ticket_invalid_ticket_number()
            - delete_ticket_invalid_data_type()



    - Service_Access_Layer

        - Ticket Cancellation:

        - Positive
            - ticket_cancellation_success()

        - Negative
            - ticket_cancellation_invalid_ticket_numer()
            - ticket_cancellation_invalid_data_type()

        - User Login:

        - Positive
            - user_login_success()
        - Negative
            - invalid_user_name()
            - invalid_password()
            - invalid_password_length()
            - invalid_username_length()


        - User Logout:

        - Positive
            - user_logout_success()



        - API

            - Successful connection to database:

            - Positive
                - successful_connection_to_database()
            - Negative
                - no_connection_to_database()

            
            - Create ticket in database:

            - Positive
                - create_ticket_database_success()
            - Negative
                - create_ticket_database_improper_values_for_schema()
                - create_ticket_not_inserted_into_database()
                - create_JSON_not_converting()


            - Read ticket in database:

            - Positive
                - reading_ticket_database_success()
            - Negative
                - reading_improper_output()

            
            - Update ticket in database:

            - Positive
                - update_ticket_database_success()
            - Negative
                - update_improper_values_for_schema()
                - update_JSON_not_converting()

            - Delete ticket in database:

            - Postive
                - delete_ticket_success()
            - Negative
                - delete_improper_values_for_schema()
                - delete_JSON_not_converting()




### Deadline

April 8th, 2022


Alex, Daniel, Jeny, Lesley Team 5