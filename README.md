## Our reimbursement application
This application was designed so that any employee could login to their employee ticket page to request reiumbursment for their business expenses. They will also be able to view and delete any tickets that they have previously made.

## Technologies Used
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
- Flask Cors

## Features
- Employees can submit a reimbursement request
- Employees can view all their reimbursement requests
- Employees can delete previous reimbursment requests


## Getting Started
- to clone:
    git clone https://github.com/dankuczynski/Project_1.git
- Database:
    create a local cloud based  Postgres RDS
    use DBeaver as our management software to set up the DB
- to deploy:
    install Flask, Pytest, pscopg[binary], Flask Cors
    run your main.py to start your connection
    on login.html file, right click and open in option, then select your browswer(currently set up for chome only)

## Usage
- Employees can log into the ticket page to manage their reiumbursement requests
    Employees can make requests
    Employees can give a reason for their reiumbursement requests
    Employees can enter amount, not exceeding $1000.00, for their reiumbursement requests
    Employees can delete their reiumbursement requests if needed.
Employees can then log out and return to the main page.