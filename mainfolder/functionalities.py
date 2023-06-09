import re

from datetime import datetime
from dbconnection import session
from models import Customer, Transaction,Loyaltypoints
from datetime import datetime
from tabulate import tabulate
from termcolor import colored 


x = "=" * 30


class Admin(): 
    # add customer 
    def add_customer():
        name = input("Enter customer name: ")
        phone_number = input("Enter customer phone: ")
        email = input("Enter customer email: ")

        if name == "" or phone_number == "" or email == "":
            print(colored("Null values not allowed!", "red"))
            return

        if len(phone_number) < 10:
            print(colored("Invalid phone number! Phone number must have at least 10 digits.", "red"))
            return

        if not re.match(r".+@gmail\.com$", email):
            print(colored("Invalid email address! Email must be in the format example@gmail.com.", "red"))
            return

        existing_customer = session.query(Customer).filter_by(email=email).first()
        if existing_customer:
            print(x)
            print(colored(f"{name} already exists!", "red"))
            print(x)
            return

        customer = Customer(name=name, phone_number=phone_number, email=email)
        session.add(customer)
        session.commit()
        print(x)
        print(colored(f"{name} has been added successfully!", "green"))
        print(x)

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
            print(x)
            print(colored("No customers found!","red"))
            print(x)
    
    # delete customer
    def delete_customer():
        customer_id = input("Enter customer ID to delete: ")
        customer = session.query(Customer).get(customer_id)
        if customer:
            session.delete(customer)
            session.commit()
            print(x)
            print(colored("Customer {name} deleted successfully!","green"))
            print(x)
        else:
            print(x)
            print(colored("Customer not found!","red"))
            print(x)

    
    
        # add transactions
# add transactions
    def add_transaction():
        customer_name = input("Enter customer name: ")
        amount = float(input("Enter transaction amount: "))
        transaction_date = datetime.now()

        customer = session.query(Customer).filter(Customer.name == customer_name).first()
        if customer:
            existing_transaction = session.query(Transaction).filter_by(customer_id=customer.id).first()
            if existing_transaction:
                # Update the existing transaction amount
                existing_transaction.amount += amount
                session.commit()
                print("Transaction amount updated successfully!")
            else:
                # Create a new transaction
                transaction = Transaction(amount=amount, transaction_date=transaction_date, customer=customer)
                session.add(transaction)
                session.commit()
                print(x)
                print(colored("Transaction added successfully!", "green"))
                print(x)

            # Calculate loyalty points
            points = int(amount / 100)  # 1 point for every 100 units
            existing_loyalty_entry = session.query(Loyaltypoints).filter_by(customer_id=customer.id).first()
            if existing_loyalty_entry:
                # Update the existing loyalty points
                existing_loyalty_entry.point += points
                session.commit()
                print(x)
                print(colored(f"Loyalty points for {customer_name} updated successfully!", "green"))
                print(x)
            else:
                # Create a new loyalty entry
                loyalty_entry = Loyaltypoints(customer_id=customer.id, point=points)  # Fix customer_id value
                session.add(loyalty_entry)
                session.commit()
                print(x)
                print(colored("Loyalty points added successfully!", "green"))
                print(x)
        else:
            print("Customer not found!")
    
    def display_loyalty_customers():
        loyalty_customers = session.query(Customer, Loyaltypoints).join(Loyaltypoints).all()

        if loyalty_customers:
            loyalty_customer_data = []
            for customer, loyalty in loyalty_customers:
                loyalty_customer_data.append([customer.id, customer.name, loyalty.point])

            headers = ["ID", "Name", "Loyalty Points"]
            print(tabulate(loyalty_customer_data, headers=headers, tablefmt="fancy_grid"))
        else:
            print(x)
            print(colored("No loyalty customers found!", "red"))
            print(x)

    


    # price redemption
    def redeem_rewards():
        customer_name = input("Enter customer name: ")
        customer = session.query(Customer).filter_by(name=customer_name).first()
        if customer:
            loyalty_points = session.query(Loyaltypoints).filter_by(customer_id=customer.id).first()
            if loyalty_points:
                available_points = loyalty_points.point
                if available_points > 0:
                    print(f"Available points for {customer_name}: {available_points}")
                    prize = input("Enter the prize you want to redeem: ")
                    points_required = int(input("Enter the points required for the prize: "))
                    if points_required <= available_points:
                        loyalty_points.point -= points_required
                        session.commit()
                        print(x)
                        print(colored(f"{customer_name} redeemed {prize} successfully! {points_required} points deducted.","green"))
                        print(x)
                    else:
                        print(x)
                        print(colored("Insufficient points for redemption.","red"))
                        print(x)
                else:
                    print(x)
                    print(colored("No loyalty points available for redemption.","red"))
                    print(x)
            else:
                print(x)
                print(colored("No loyalty points found for this customer.","red"))
                print(x)
        else:
            print(x)
            print("Customer not found!")
            print(x)