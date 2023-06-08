import click
from functionalities import Admin


@click.group()
def loyalty_app():
    """
    Loyalty Management App - Manage customers, transactions, and loyalty points.
    """
    pass


@loyalty_app.command()
def add_customer():
    """
    Add a new customer.
    """
    Admin.add_customer()


@loyalty_app.command()
def add_transaction():
    """
    Add a transaction.
    """
    Admin.add_transaction()


@loyalty_app.command()
def display_customers():
    """
    Display all customers.
    """
    Admin.display_customers()


@loyalty_app.command()
def delete_customer():
    """
    Delete a customer.
    """
    Admin.delete_customer()


@loyalty_app.command()
def display_loyalty_points():
    """
    Display loyalty points for all customers.
    """
    Admin.display_loyalty_points()


@loyalty_app.command()
def redeem_rewards():
    """
    Redeem rewards for a customer.
    """
    Admin.redeem_rewards()


def main():
    loyalty_app()


if __name__ == "__main__":
    main()
