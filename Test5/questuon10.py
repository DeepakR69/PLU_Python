# # 10. Sales Performance Dashboard
# ### Problem Statement
# A retail company stores sales information.
# Each sale contains:
# * Salesperson ID
# * Product
# * Quantity
# * Revenue
# * Region
# ### Requirements
# 1. Retrieve all sales records.
# 2. Sort records based on revenue.
# 3. Search a salesperson using Employee ID.
# 4. Display Top 5 salespersons.
# 5. Find the highest revenue region.
# 6. Update monthly incentive status for eligible salespersons.
# ### Concepts
# * SQL GROUP BY
# * Sorting
# * Binary Search
# * Dictionaries
# * SQLite
import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    employee_id INTEGER,
    name TEXT,
    product TEXT,
    quantity INTEGER,
    revenue REAL,
    region TEXT,
    incentive_status TEXT
)
""")

sales = [
    (101,"Deepak","Laptop",5,250000,"North","Pending"),
    (102,"Rahul","Mobile",8,160000,"South","Pending"),
    (103,"Priya","Tablet",6,180000,"East","Pending"),
    (104,"Neha","Laptop",7,350000,"North","Pending"),
    (105,"Amit","Monitor",4,120000,"West","Pending"),
    (106,"Rohan","Printer",10,220000,"South","Pending")
]

cursor.executemany(
    "INSERT INTO sales VALUES(?,?,?,?,?,?,?)",
    sales
)

conn.commit()
conn.close()

print("Database Created Successfully")
import sqlite3


# --------------------------
# Sales Class
# --------------------------

class Sale:

    def __init__(self, employee_id, name, product,
                 quantity, revenue, region,
                 incentive_status):

        self.employee_id = employee_id
        self.name = name
        self.product = product
        self.quantity = quantity
        self.revenue = revenue
        self.region = region
        self.incentive_status = incentive_status

    def display(self):

        print(f"""
Employee ID : {self.employee_id}
Name        : {self.name}
Product     : {self.product}
Quantity    : {self.quantity}
Revenue     : {self.revenue}
Region      : {self.region}
Incentive   : {self.incentive_status}
""")


# --------------------------
# Fetch Sales
# --------------------------

def fetch_sales():

    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")

    rows = cursor.fetchall()

    conn.close()

    sales = []

    for row in rows:
        sales.append(Sale(*row))

    return sales


# --------------------------
# Binary Search
# --------------------------

def binary_search(arr, target):

    left = 0
    right = len(arr)-1

    while left <= right:

        mid = (left+right)//2

        if arr[mid].employee_id == target:
            return arr[mid]

        elif arr[mid].employee_id < target:
            left = mid + 1

        else:
            right = mid - 1

    return None


# --------------------------
# Top 5 Salespersons
# --------------------------

def top_five(arr):

    print("\nTop 5 Salespersons\n")

    top = sorted(arr,
                 key=lambda x:x.revenue,
                 reverse=True)

    for sale in top[:5]:
        sale.display()

def highest_region(arr):

    revenue = {}

    for sale in arr:

        revenue[sale.region] = revenue.get(
            sale.region,0
        ) + sale.revenue

    region = max(revenue,key=revenue.get)

    print("\nHighest Revenue Region")
    print(region,"-",revenue[region])


# --------------------------
# Update Incentive
# --------------------------

def update_incentive():

    conn = sqlite3.connect("sales.db")

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE sales
    SET incentive_status='Eligible'
    WHERE revenue>=200000
    """)

    conn.commit()
    conn.close()

    print("\nIncentive Status Updated")
    

# --------------------------
# Main
# --------------------------

sales = fetch_sales()

# Sort by Revenue

sales.sort(key=lambda x:x.revenue,
           reverse=True)

print("\nSales Sorted by Revenue\n")

for sale in sales:
    sale.display()

# Binary Search

sales.sort(key=lambda x:x.employee_id)

emp = int(input("Enter Employee ID: "))

result = binary_search(sales,emp)

if result:
    print("\nEmployee Found")
    result.display()
else:
    print("Employee Not Found")

top_five(sales)
highest_region(sales)
update_incentive()