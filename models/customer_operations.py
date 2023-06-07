from datetime import datetime
from dbconnection import session
from models import Customer, Transaction
from datetime import datetime

 
def add_customer():
    # customer should not be able to enter null values
    # if customer exist should not be able to added twice
     
     name = input("Enter customer name: ")
     phone_number = input("Enter customer phone: ")
     email = input("Enter customer email: ")
     
 
     customer = Customer(name=name, phone_number=phone_number, email=email)
     session.add(customer)
     session.commit()
     print("Customer added successfully!")
 
 
def add_transaction():
    # culculate point base on amount 
    #colum return  customer name instead of id 
     customer_name = input("Enter customer name: ")
     amount = input("Enter transaction amount: ")
     transaction_date = datetime.now()
 
     customer = session.query(Customer).filter(Customer.name == customer_name).first()
     if customer:
         transaction = Transaction(amount=amount, transaction_date=transaction_date, customer=customer)
         session.add(transaction)
         session.commit()
         print("Transaction added successfully!")
     else:
         print("Customer not found!")
 
 
 
 ##########################
 def update_point_balance():
    user_id = input("User ID: ")
    user = session.query(User).filter(User.id == user_id).first()

    if user:
        point_balance = session.query(PointBalance).filter(PointBalance.user_id == user_id).first()
        if point_balance:
            # Calculate the total points earned by the user
            total_points = sum(transaction.amount // 10 for transaction in user.transactions)
            point_balance.total_points = total_points
        else:
            
    
 
 
 ##########################

#add = add_customer()
add2 = add_transaction()
 
 
print(add2)
#print(add2)