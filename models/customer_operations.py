from datetime import datetime
from dbconnection import session
from models import Customer, Transaction
from datetime import datetime

def add_customer():
    name = input("Enter customer name: ")
    phone = int(input("Enter customer phone: "))
    email = input("Enter customer email: ")

    customer = Customer(name=name, phone=phone, email=email)
    session.add(customer)
    session.commit()
    print("Customer added successfully!")


def add_transaction():
    customer_id = int(input("Enter customer ID: "))
    amount = int(input("Enter transaction amount: "))
    transaction_date = datetime.now()

    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        transaction = Transaction(amount=amount, transaction_date=transaction_date, customer=customer)
        session.add(transaction)
        session.commit()
        print("Transaction added successfully!")
    else:
        print("Customer not found!")




add = add_transaction()


print(add)



