# Loyalty App

The Loyalty App is a customer loyalty management system designed to help businesses effectively manage and track their customer loyalty programs. With this app, businesses can easily store customer information, track customer transactions, manage loyalty points, and provide rewards to customers.

# Features

-Add new customers: Administrators can add new customers by providing their name, phone number, and email address. Duplicate entries are not allowed.

-Display customers: Administrators can view a table of all the customers along with their details such as ID, name, phone number, and email address.

-Delete customer: Administrators can delete a customer by providing their ID.

-Add transactions: Administrators can add transactions for customers by specifying the customer name, transaction amount, and date. The transaction amount is added to the existing transaction or creates a new transaction if none exists. Loyalty points are calculated based on the transaction amount and added to the existing loyalty points or created as a new entry.

-Display loyalty points: Administrators can view a table of all the customers' loyalty points along with their respective names.

-Redeem rewards: Administrators can redeem rewards for a specific customer by selecting a prize and deducting the corresponding loyalty points. Administrators can specify the customer name, the prize to redeem, and the points required for redemption. The loyalty points are deducted if the customer has sufficient points.

# Usage

To run the Loyalty App, follow these steps:

-Install the required dependencies by running the following commands:
pipenv install sqlalchemy
pip install tabulate
-Start the Loyalty App by running the main application file.
-Access the Loyalty App through the local server.
-Use the app to add new customers, display customers, delete customers, add transactions, display loyalty points, and redeem rewards.

# Technology Stack

The Loyalty App is built using the following technologies:

Python: The core programming language used for backend development.
SQLAlchemy: A powerful SQL toolkit and Object-Relational Mapping (ORM) library for managing the database.

# Future Enhancements

Integration with external payment gateways for seamless transaction recording.
Advanced analytics and reporting features to generate actionable insights.
Integration with customer communication channels (e.g., email, SMS) for targeted marketing campaigns.
Mobile app development for enhanced customer engagement.
Multi-store support to cater to businesses with multiple locations.

# Contributors

Erick Kirui
Sang Kibet
Phoebe Oigara
Abednego Kibiwott

Copyright (c) [2023] [Soweto]