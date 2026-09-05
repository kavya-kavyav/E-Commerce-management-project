
from db import get_connection


def print_customers(customers):
    for customer in customers:
        print(f"details of customer id : {customer[0]}")
        print(f"customer name: {customer[1]}")
        print(f"customer email: {customer[2]}")
        print(f"customer phone: {customer[3]}")
        print("********************************33")


def get_all_customers():
    connection = get_connection()
    query = "select * from customers"
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    print_customers(res)
    cursor.close()
    connection.close()


def print_customer_by_id(customer):
    print(f"details of customer id: {customer[0]}")
    print(f"customer name: {customer[1]}")
    print(f"customer email: {customer[2]}")
    print(f"customer phone: {customer[3]}")


def get_customer_by_id(customer_id):
    connection = get_connection()
    query = "select * from customers where customer_id = %s"
    cursor = connection.cursor()
    cursor.execute(query, (customer_id,))
    customer = cursor.fetchone()

    if customer:
        print_customer_by_id(customer)
    else:
        print("customer not found")

    cursor.close()
    connection.close()


def create_customer_in_db():
    name = input("enter customer name: ")
    email = input("enter customer email: ")
    phone = input("enter customer phone: ")

    connection = get_connection()
    query = """
    insert into customers(name, email, phone_no)
    values (%s, %s, %s)
    """

    cursor = connection.cursor()
    cursor.execute(query, (name, email, phone))
    connection.commit()

    print("customer added successfully")

    cursor.close()
    connection.close()


def delete_customer_data():
    customer_id = int(input("enter customer id: "))

    connection = get_connection()
    query = "delete from customers where customer_id = %s"

    cursor = connection.cursor()
    cursor.execute(query, (customer_id,))
    connection.commit()

    print("customer data deleted successfully")

    cursor.close()
    connection.close()


def update_customer_data():
    customer_id = int(input("enter customer id to be update: "))
    name = input("enter customer name: ")
    email = input("enter customer email: ")
    phone = input("enter customer phone: ")

    connection = get_connection()

    query = """
    update customers
    set name = %s, email = %s, phone = %s
    where customer_id = %s
    """

    cursor = connection.cursor()
    cursor.execute(query, (name, email, phone, customer_id))
    connection.commit()

    print("customer data updated successfully")

    cursor.close()
    connection.close()