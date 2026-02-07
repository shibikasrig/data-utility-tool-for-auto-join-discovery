import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE customers (customer_id INTEGER, name TEXT, email TEXT)")
cursor.execute("CREATE TABLE orders (order_id INTEGER, customer_id INTEGER, order_date TEXT)")
cursor.execute("CREATE TABLE payments (payment_id INTEGER, order_id INTEGER, amount REAL)")
cursor.execute("CREATE TABLE products (product_id INTEGER, name TEXT, price REAL)")

conn.commit()
conn.close()

print("Database created successfully")
