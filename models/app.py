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
    
    # delete customer
    def delete_customer():
        customer_id = input("Enter customer ID to delete: ")
        customer = session.query(Customer).get(customer_id)
        if customer:
            session.delete(customer)
            session.commit()
            print("Customer deleted successfully!")
        else:
            print("Customer not found!")

    
    
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
                print("Transaction added successfully!")

            # Calculate loyalty points
            points = int(amount / 100)  # 1 point for every 100 units
            existing_loyalty_entry = session.query(Loyaltypoints).filter_by(customer_id=customer.id).first()
            if existing_loyalty_entry:
                # Update the existing loyalty points
                existing_loyalty_entry.point += points
                session.commit()
                print("Loyalty points updated successfully!")
            else:
                # Create a new loyalty entry
                loyalty_entry = Loyaltypoints(customer_id=customer.id, point=points)
                session.add(loyalty_entry)
                session.commit()
                print("Loyalty points added successfully!")
        else:
            print("Customer not found!")



            from sqlalchemy import create_engine, PrimaryKeyConstraint, UniqueConstraint, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///database/loyalty.db', echo=True)


class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='id_pk'),
        UniqueConstraint('email', 'name', name='uix_1'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    transactions = relationship("Transaction", back_populates="customer")


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Integer)
    transaction_date = Column(DateTime)
    customer = relationship("Customer", back_populates="transactions")

    customer_name = relationship("Customer", back_populates="transactions", uselist=False, foreign_keys=[customer_id], overlaps="customer")


class Loyaltypoints(Base):
    __tablename__ = 'loyaltypoints'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    point = Column(Integer)


# delete tables
#Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


    
 
 


