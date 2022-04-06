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
- Cucumber
- Selenium
- Chomerdriver
- geckodriver
- IEDriverServer
- Behave


### Scope

- Entities:
    - Employee(
        employee_id int Primary Key,
        username varchar(20),
        password varchar(20)
    );


    - Ticket(
        ticket_number serial primary key,
        employee_id int foreign key,        
        reimbursement_reason varchar(100),
        reimbursement_ticket_amount float

    );

- Testing plan

    - Data_Access_Layer
      - Employee_DAO
        - create_ticket_success(1.1)
            - create_ticket_reason_invalid_datatype(1.2)
            - create_ticket_empty_string(1.3)
            - create_ticket_excess_amount(1.4)
            - create_ticket_zero_and_less_than_zero(1.5)

        - get_all_ticket_by_employee_id_success(1.6)

        - delete_ticket_success(1.7)
            - delete_ticket_invalid_data_type(1.8)
            - delete_ticket_invalid_ticket_number(1.9)

        - get_username_success(2.1)
            - get_employee_username_invalid_id(2.2)
            - get_employee_password_by_id(2.3)
            - get_read_employee_password_invalid_id(2.4)


            - get_all_tickets_invalid_employee_id(?)
            - get_all_tickets_invalid_datatype(?)


    - Service_Access_Layer

        - Ticket SAL:
            - check_non_int_employee_id(3.1)
            - check_non_str_reimbursement_reason(3.2)
            - check_non_float_ticekt_amount(3.3)
            - check_reimbursement_reason_length(3.4)
            - check_ticket_amount_over_limit(3.5)
            - check_ticket_amount_under_limit(3.6) 
            
            - ticket_cancellation_success(3.7)
                - ticket_cancellation_invalid_ticket_number(3.8)
                - ticket_cancellation_invalid_ticket_number_data_type(3.9)

            - user_login_success(4.1)
                - test_invalid_username(4.2)
                - test_invalid_password(4.3)
                - test_invalid_password_length(4.4)
                - test_invalid_username_length(4.5)



        - API
            - successful_connection_to_database(5.1)
                - no_connection_to_database()

            - create_ticket_database_success(5.2)
                - create_ticket_database_improper_values_for_schema()
                - create_ticket_not_inserted_into_database()
                - create_JSON_not_converting()


            - reading_ticket_database_success(5.3)
                - reading_improper_output()


            - delete_ticket_success(5.4)
                - delete_improper_values_for_schema()
                - delete_JSON_not_converting()




### Deadline

April 8th, 2022


Alex, Daniel, Jeny, Lesley Team 5