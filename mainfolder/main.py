from functionalities import Admin

# from customer_operations import Admin
from termcolor import colored

x = 30 * '='

def display_menu():
    print(x)
    print(colored("""
WELCOME TO THE LOYALTY APP
    ""","green"))
    print(x)
    print("  ")
    print(colored("What would you like to do: ","green"))
    print("  ")
    print(colored("1. Add a customer","cyan"))
    print(colored("2. View all customers","cyan"))
    print(colored("3. Delete customers","cyan"))
    print(colored("4. Add transaction","cyan"))
    print(colored("6. Display Loyal customer points","cyan"))
    print(colored("7. Redeem points","cyan"))
    print(colored("8. Show Version","cyan"))
    print(colored("0. Exit","cyan"))

    


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
            Admin.display_customers()
            
        elif choice == "3":
            Admin.delete_customer()

        elif choice == "4":
            Admin.add_transaction()
        
        elif choice == "6":
            Admin.display_loyalty_customers()

        elif choice == "7":
            Admin.redeem_rewards()
        
        elif choice == "8":
            Admin.show_version()
        else:
            print(colored("Invalid choice! Please try again.","red"))


if __name__ == "__main__":
    main()