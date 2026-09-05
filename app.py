from db import get_connection

from customers import get_all_customers
from customers import get_customer_by_id
from customers import create_customer_in_db
from customers import delete_customer_data
from customers import update_customer_data

from products import get_all_products
from products import get_product_by_id
from products import create_product_in_db
from products import delete_product_data
from products import update_product_data

from orders import get_all_orders
from orders import create_order_in_db
from orders import delete_order_data
from orders import update_order_status


print("====== E-Commerce Management App =====")

print("Click 1  : To see all customers")
print("Click 2  : To see customer by id")
print("Click 3  : To add customer")
print("Click 4  : To delete customer")
print("Click 5  : To update customer")

print("Click 6  : To see all products")
print("Click 7  : To see product by id")
print("Click 8  : To add product")
print("Click 9  : To delete product")
print("Click 10 : To update product")

print("Click 11 : To place order")
print("Click 12 : To see all orders")
print("Click 13 : To delete order")
print("Click 14 : To update order status")

print("Click 15 : Exit")


while True:

    choice = input("What you want to perform: ")

    if choice == "1":
        get_all_customers()

    elif choice == "2":
        customer_id = int(input("enter customer id: "))
        get_customer_by_id(customer_id)

    elif choice == "3":
        create_customer_in_db()

    elif choice == "4":
        delete_customer_data()

    elif choice == "5":
        update_customer_data()

    elif choice == "6":
        get_all_products()

    elif choice == "7":
        product_id = int(input("enter product id: "))
        get_product_by_id(product_id)

    elif choice == "8":
        create_product_in_db()

    elif choice == "9":
        delete_product_data()

    elif choice == "10":
        update_product_data()

    elif choice == "11":
        create_order_in_db()

    elif choice == "12":
        get_all_orders()

    elif choice == "13":
        delete_order_data()

    elif choice == "14":
        update_order_status()

    elif choice == "15":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
        