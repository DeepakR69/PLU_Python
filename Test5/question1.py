# # 1. Smart Inventory Management System
# ### Problem Statement
# An e-commerce warehouse stores product information in an SQLite database.
# Each product has:
# * Product ID
# * Product Name
# * Category
# * Quantity
# * Price
# ### Requirements
# 1. Fetch all products from the SQLite database.
# 2. Store them in Python objects.
# 3. Sort the products based on quantity using **Merge Sort**.
# 4. Allow the manager to search for a Product ID using **Binary Search**.
# 5. Display the complete product details.
# 6. Display products whose stock is below 10.
# ### Concepts
# * SQLite
# * Python Classes
# * Merge Sort
# * Binary Search
# * SQL SELECT
import sqlite3

conn = sqlite3.connect("inventory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL
)
""")

products = [
    (101, "Laptop", "Electronics", 12, 65000),
    (102, "Mouse", "Electronics", 8, 700),
    (103, "Keyboard", "Electronics", 15, 1200),
    (104, "Monitor", "Electronics", 5, 15000),
    (105, "Chair", "Furniture", 20, 3500),
    (106, "Table", "Furniture", 7, 6000),
    (107, "Notebook", "Stationery", 50, 80),
    (108, "Pen", "Stationery", 4, 20)
]

cursor.executemany(
    "INSERT OR REPLACE INTO products VALUES(?,?,?,?,?)",
    products
)

conn.commit()
conn.close()

print("Database Created Successfully")