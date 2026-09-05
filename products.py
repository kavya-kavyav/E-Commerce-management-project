

from db import get_connection


def print_products(products):
    for product in products:
        print(f"details of product id : {product[0]}")
        print(f"product name: {product[1]}")
        print(f"product price: {product[2]}")
        print(f"product stock: {product[3]}")
        print(f"category: {product[4]}")
        print(f"brand: {product[5]}")
        print(f"description: {product[6]}")
        print(f"rating: {product[7]}")
        print("*********")


def get_all_products():
    connection = get_connection()
    query = "select * from products"
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    print_products(res)
    cursor.close()
    connection.close()


def print_product_by_id(product):
    print(f"details of product id: {product[0]}")
    print(f"product name: {product[1]}")
    print(f"product price: {product[2]}")
    print(f"product stock: {product[3]}")
    print(f"category: {product[4]}")
    print(f"brand: {product[5]}")
    print(f"description: {product[6]}")
    print(f"rating: {product[7]}")
    print("*********")


def get_product_by_id(product_id):
    connection = get_connection()
    query = "select * from products where product_id = %s"
    cursor = connection.cursor()
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()

    if product:
        print_product_by_id(product)
    else:
        print("product not found")

    cursor.close()
    connection.close()


def create_product_in_db():
    name = input("enter product name: ")
    price = float(input("enter product price: "))
    stock = int(input("enter product stock: "))
    category = input("enter category: ")
    brand = input("enter brand: ")
    description = input("enter description: ")
    rating = float(input("enter rating: "))

    connection = get_connection()

    query = """
    insert into products(product_name, price, stock,category, brand, description, rating)
    values (%s, %s, %s,%s,%s,%s,%s)
    """

    cursor = connection.cursor()
    cursor.execute(query, (name, price, stock,category, brand, description,rating))
    connection.commit()

    print("product added successfully")

    cursor.close()
    connection.close()


def delete_product_data():
    product_id = int(input("enter product id: "))

    connection = get_connection()
    query = "delete from products where product_id = %s"

    cursor = connection.cursor()
    cursor.execute(query, (product_id,))
    connection.commit()
    if cursor.rowcount > 0:
        connection.commit()
        print("product data deleted successfully")
    else:
        print("product not found")

    cursor.close()
    connection.close()


def update_product_data():
    product_id = int(input("enter product id to be update: "))
    name = input("enter product name: ")
    price = float(input("enter product price: "))
    stock = int(input("enter product stock: "))

    connection = get_connection()

    query = """
    update products
    set product_name = %s, price = %s, stock = %s
    where product_id = %s
    """

    cursor = connection.cursor()
    cursor.execute(query, (name, price, stock, product_id))
    connection.commit()

    print("product data updated successfully")

    cursor.close()
    connection.close()   