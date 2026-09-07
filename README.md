Mini E-Commerce Order Management System

Project Overview

The Mini E-Commerce Order Management System is a console-based application developed using Python and MySQL.

The project helps manage:

Customer information

Product information

Product features such as category, brand, description, and rating

Product stock

Customer orders

Order status

Payment status

The application uses PyMySQL to connect Python with the MySQL database.

A simple owner password authentication feature is also included. Only the owner can add, update, or delete products and modify/delete orders.

Problem Statement

Managing customers, products, stock, and orders manually can cause data duplication, incorrect stock information, and difficulties in tracking orders.

The objective of this project is to create a simple system that stores customer and product information, processes orders, calculates the total amount, updates product stock, and restricts important management operations to the owner.

Technologies Used

Python

MySQL

PyMySQL

SQL

VS Code

Project Structure

E-Commerce/
│
├── app.py
├── db.py
├── auth.py
├── customers.py
├── products.py
└── orders.py

File Description

File

Purpose

app.py

Main menu and controls the application

db.py

Establishes connection with MySQL

auth.py

Checks the owner password

customers.py

Customer operations

products.py

Product operations

orders.py

Order processing and order operations

Database

The project uses the following database:

CREATE DATABASE e_commerce_order_management_system;

Customers Table

Stores customer information.

Column

Description

customer_id

Primary key

name

Customer name

email

Customer email

phone_no

Customer phone number

Products Table

Stores product information.

Column

Description

product_id

Primary key

product_name

Product name

price

Product price

stock

Available stock

category

Product category

brand

Product brand

description

Product description

rating

Product rating

Orders Table

Stores order information.

Column

Description

order_id

Primary key

customer_id

Foreign key from customers

product_id

Foreign key from products

quantity

Quantity ordered

total_amount

Total order amount

order_status

Current order status

payment_status

Payment status

Database Relationships

Customers
    |
    | customer_id
    |
    v
  Orders
    ^
    |
    | product_id
    |
Products

One customer can place multiple orders.

A product can appear in multiple orders.

customer_id connects customers and orders.

product_id connects products and orders.

Main Features

1. Customer Management

The application allows you to:

View all customers

Search customer by ID

Add a new customer

Delete customer data

Update customer information

If the entered customer ID does not exist, the application displays:

Customer not available

2. Product Management

The owner can:

Add products

View all products

Search products

Update products

Delete products

Product information includes:

Name

Price

Stock

Category

Brand

Description

Rating

3. Order Management

The application can:

Place an order

View all orders

Delete an order

Update order status

Track payment status

When an order is placed:

The system checks whether the customer exists.

The system checks whether the product exists.

The system checks available stock.

The total amount is calculated.

The order is inserted into the database.

Product stock is automatically reduced.

Example:

Product price = 1500
Quantity = 2

Total amount = 1500 × 2
             = 3000

Owner Authentication

The project contains a simple owner authentication system.

The owner password is stored in auth.py.

OWNER_PASSWORD = "12345"

The password is required for operations that modify important product and order data.

Password Protected Operations

Operation

Password Required

View products

No

Search products

No

Add product

Yes

Update product

Yes

Delete product

Yes

View orders

No

Place order

No

Update order status

Yes

Delete order

Yes

Note: The hard-coded password is suitable for this educational project. A real application should use secure password hashing and proper user authentication.

Installation

Step 1: Install Python

Make sure Python is installed on your system.

Check:

python --version

Step 2: Install PyMySQL

Run:

pip install pymysql

Step 3: Install MySQL

Make sure MySQL Server is running.

You can use MySQL Workbench, phpMyAdmin, or another MySQL client.

Database Setup

Create the database:

CREATE DATABASE e_commerce_order_management_system;

Select it:

USE e_commerce_order_management_system;

Create the tables according to the project structure described above.

Make sure the column names in MySQL match the names used in the Python files.

For example, the customer phone column used by the project is:

phone_no

Configure Database Connection

Open db.py and configure your MySQL credentials:

from pymysql import connect


def get_connection():

    connection = connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="e_commerce_order_management_system"
    )

    return connection

Replace YOUR_PASSWORD with your local MySQL password.

Run the Project

Open the project folder in VS Code terminal.

Run:

python app.py

The application displays a menu similar to:

====== E-Commerce Management App ======

1. View all customers
2. Search customer
3. Add customer
4. Delete customer
5. Update customer

6. Add product
7. Delete product
8. Update product
9. View products
10. Search product

11. Place order
12. Delete order
13. Update order status
14. View orders

15. Exit

Enter the number of the operation you want to perform.

Example Order Process

What you want to perform: 11

Enter customer id: 4
Enter product id: 1
Enter quantity: 2

Order placed successfully
Total amount: 110000

The system also decreases the product stock automatically.

SQL Concepts Used

This project demonstrates several important SQL concepts:

CREATE DATABASE

CREATE TABLE

INSERT

SELECT

UPDATE

DELETE

WHERE

JOIN

Primary Key

Foreign Key

AUTO_INCREMENT

NOT NULL

UNIQUE

Constraints

Example JOIN used to display order information:

SELECT
    o.order_id,
    c.name,
    p.product_name,
    o.quantity,
    o.total_amount,
    o.order_status,
    o.payment_status
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN products p
ON o.product_id = p.product_id;

Python Concepts Used

The project demonstrates:

Functions

Modules

Imports

User input

Conditional statements

Loops

Exception/database error handling concepts

MySQL connectivity

SQL queries from Python

CRUD operations

Advantages

Simple and beginner-friendly

Modular Python structure

Easy customer management

Easy product management

Automatic order calculation

Automatic stock update

Foreign key relationships

Owner authorization for sensitive operations

Easy to extend

Future Enhancements

The project can be improved by adding:

Secure password hashing

Customer login

Shopping cart

Product categories table

Multiple products in a single order

Payment gateway integration

Invoice generation

Sales reports

Monthly revenue analysis

Product search by category or brand

Low-stock alerts

GUI using Tkinter

Web application using Flask or Django

Author

Kavya

B.Tech CSE (AI & ML)

Conclusion

The Mini E-Commerce Order Management System demonstrates how Python can be integrated with MySQL to build a practical database application.

It provides customer, product, and order management while using SQL relationships and basic owner authentication to protect important operations.
