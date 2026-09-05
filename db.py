from pymysql import connect
def get_connection():
    connection = connect(
        host = "localhost",
        user = "root",
        password = "Kavya@0987",
        database = "e_commerce_order_management_system"
    )
    return connection