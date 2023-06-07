from datetime import datetime
from dbconnection import session
from models import Customer, Transaction

def add_customer():
    name = input("Enter customer name: ")
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    print("Customer added successfully!")

def add_transaction():
    user_id = input("User ID: ")
    amount = int(input("Transaction Amount: "))
    transaction_date = datetime.now()

    customer = session.query(Customer).filter(Customer.id == user_id).first()
    if customer:
        transaction = Transaction(amount=amount, datetime=transaction_date, customer=customer)
        session.add(transaction)
        session.commit()
        print("Transaction added successfully!")
    else:
        print("Customer not found!")
