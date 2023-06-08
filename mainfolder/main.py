from functionalities import Admin

x = 30 * '='

def display_menu():
    
    print("""
WELCOME TO THE LOYALTY APP
    """)
    print(x)
    print("  ")
    print("What would you like to do: ")
    print("  ")
    print("1. Add a customer")
    print("2. Add a transaction")
    print("3. View all customers")
    print("4. Delete customers")
    print("5. Display loyal customer points")
    print("6. See points for specific client")
    print("7. Redeem points")
    print("0. Exit")

    


def main():
    while True:

        display_menu()
        print("  ")
        choice = input("Enter your choice: ")

        print(x)

        if choice == "0":
            print("  ")
            print("We miss you already!")
            print("  ")
            break
        elif choice == "1":
            Admin.add_customer()
        elif choice == "2":
            Admin.add_transaction()

        elif choice == "3":
            Admin.display_customers()

        elif choice == "4":
            Admin.delete_customer()

        elif choice == "5":
            Admin.display_loyalty_points()
        
        elif choice == "6":
            Admin.display_loyalty_points()

        elif choice == "7":
            Admin.redeem_rewards()
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()