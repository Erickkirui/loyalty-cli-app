#start here
def calculate_points():
    transaction_id = input("Transaction ID: ")
    transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction:
        # Calculate points based on transaction amount (e.g., 1 point per $10 spent)
        points_earned = transaction.amount // 10
        print(f"Points earned: {points_earned}")
    else:
        print("Transaction not found!")
        
def add_customer():
    name = input("Enter customer name: ")
    
    existing_customer = session.query(Customer).filter(Customer.name == name).first()
    if existing_customer:
        print("Customer already exists.")
    else:
        new_customer = Customer(name=name)
        session.add(new_customer)
        session.commit()
        print("New customer added successfully!")