from customer_operations import Admin

x = 30 * '='

def display_menu():
    print(x)
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
    print("4. delete customers")
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
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()