from db_config import connect

def get_products_by_price():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_code, product_name, list_price, discount_percent
        FROM Products
        ORDER BY list_price DESC;
    """)
    return cursor.fetchall()

def get_customers_full_name_m_to_z():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name,
               CONCAT(last_name, ', ', first_name) AS full_name
        FROM Customers
        WHERE last_name >= 'M'
        ORDER BY last_name ASC;
    """)
    return cursor.fetchall()

def get_midpriced_products_by_date():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_name, list_price, date_added
        FROM Products
        WHERE list_price > 500 AND list_price < 2000
        ORDER BY date_added DESC;
    """)
    return cursor.fetchall()

def get_order_item_totals():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT item_id,
               item_price,
               discount_amount,
               quantity,
               item_price * quantity AS price_total,
               discount_amount * quantity AS discount_total,
               (item_price - discount_amount) * quantity AS item_total
        FROM Order_Items
        WHERE (item_price - discount_amount) * quantity > 500
        ORDER BY item_total DESC;
    """)
    return cursor.fetchall()

def get_product_categories():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category_name, product_name, list_price
        FROM Categories
        JOIN Products ON Categories.category_id = Products.category_id
        ORDER BY category_name ASC, product_name ASC;
    """)
    return cursor.fetchall()

def get_addresses_by_email(email):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT first_name, last_name, email_address, line1, city, state, zip_code
        FROM Customers
        JOIN Addresses ON Customers.customer_id = Addresses.customer_id
        WHERE email_address = %s
        ORDER BY zip_code ASC;
    """
    cursor.execute(query, (email,))
    return cursor.fetchall()

def get_shipping_addresses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name, line1, city, state, zip_code
        FROM Customers
        JOIN Addresses ON Customers.customer_id = Addresses.customer_id
        WHERE address_type = 'shipping'
        ORDER BY zip_code ASC;
    """)
    return cursor.fetchall()
