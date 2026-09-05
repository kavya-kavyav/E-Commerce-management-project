from db import get_connection


def print_orders(orders):
    for order in orders:
        print(f"order id: {order[0]}")
        print(f"customer name: {order[1]}")
        print(f"product name: {order[2]}")
        print(f"quantity: {order[3]}")
        print(f"total amount: {order[4]}")
        print(f"order status: {order[5]}")
        print("*********")


def get_all_orders():
    connection = get_connection()

    query = """
    select o.order_id, c.name, p.product_name,
           o.quantity, o.total_amount, o.order_status
    from orders o
    join customers c
    on o.customer_id = c.customer_id
    join products p
    on o.product_id = p.product_id
    """

    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()

    print_orders(res)

    cursor.close()
    connection.close()


def create_order_in_db():
    customer_id = int(input("enter customer id: "))
    product_id = int(input("enter product id: "))
    quantity = int(input("enter quantity: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    select price, stock
    from products
    where product_id = %s
    """

    cursor.execute(query, (product_id,))
    product = cursor.fetchone()

    if product is None:
        print("product not found")

    else:
        price = product[0]
        stock = product[1]

        if quantity > stock:
            print("not enough stock")

        else:
            total_amount = price * quantity

            query = """
            insert into orders
            (customer_id, product_id, quantity, total_amount)
            values (%s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (customer_id, product_id, quantity, total_amount)
            )

            query = """
            update products
            set stock = stock - %s
            where product_id = %s
            """

            cursor.execute(query, (quantity, product_id))

            connection.commit()

            print("order placed successfully")
            print(f"total amount: {total_amount}")

    cursor.close()
    connection.close()


def delete_order_data():
    order_id = int(input("enter order id: "))

    connection = get_connection()
    query = "delete from orders where order_id = %s"

    cursor = connection.cursor()
    cursor.execute(query, (order_id,))
    connection.commit()

    print("order data deleted successfully")

    cursor.close()
    connection.close()


def update_order_status():
    order_id = int(input("enter order id: "))
    status = input("enter order status: ")

    connection = get_connection()

    query = """
    update orders
    set order_status = %s
    where order_id = %s
    """

    cursor = connection.cursor()
    cursor.execute(query, (status, order_id))
    connection.commit()

    print("order status updated successfully")

    cursor.close()
    connection.close()
    