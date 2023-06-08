from datetime import datetime
from dbconnection import session
from models import Customer, Transaction,Loyaltypoints
from datetime import datetime
from tabulate import tabulate



class Admin(): 
    # add customer 
    def add_customer():
        # customer should not be able to enter null values
        # if customer exist should not be able to added twice
        
        name = input("Enter customer name: ")
        phone_number = input("Enter customer phone: ")
        email = input("Enter customer email: ")

        if name == "" or phone_number == "" or email == "":
            print("Null values not allowed!")
            return

        existing_customer = session.query(Customer).filter_by(email=email).first()
        if existing_customer:
            print(f"{name} already exists!")
            return
        
    
        customer = Customer(name=name, phone_number=phone_number, email=email)
        session.add(customer)
        session.commit()
        print(f"{name} has been added successfully!")

    # display customers
    def display_customers():
        customers = session.query(Customer).all()
        if customers:
            customer_data = []
            for customer in customers:
                customer_data.append([customer.id, customer.name, customer.phone_number, customer.email])

            headers = ["ID", "Name", "Phone Number", "Email"]
            print(tabulate(customer_data, headers=headers, tablefmt="fancy_grid"))
        else:
            print("No customers found!")

    
    

    def add_transaction():
        customer_name = input("Enter customer name: ")
        amount = float(input("Enter transaction amount: "))
        transaction_date = datetime.now()

        customer = session.query(Customer).filter(Customer.name == customer_name).first()
        if customer:
            transaction = Transaction(amount=amount, transaction_date=transaction_date, customer=customer)
            session.add(transaction)
            session.commit()
            print("Transaction added successfully!")

            # Calculate loyalty points
            points = int(amount / 100)  # 1 point for every 100 units
            loyalty_entry = Loyaltypoints(customer_id=customer.name, point=points)
            session.add(loyalty_entry)
            session.commit()
            print("Loyalty points added successfully!")
        else:
            print("Customer not found!")

    
 
 


