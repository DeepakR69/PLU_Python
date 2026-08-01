#  8. Ride Booking Management System
# ### Problem Statement
# A cab company stores:
# Drivers
# Customers
# Bookings
# ### Requirements
# 1. Fetch available drivers.
# 2. Store them in a Graph representing city connectivity.
# 3. Find the nearest available driver using **BFS**.
# 4. Assign the booking.
# 5. Update driver availability.
# ### Concepts
# * Graph
# * BFS
# * SQL JOIN
# * UPDATE
import sqlite3

conn = sqlite3.connect("ride_booking.db")
cursor = conn.cursor()

# Drivers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS drivers(
    driver_id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT,
    available INTEGER
)
""")

# Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT
)
""")

# Bookings Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    driver_id INTEGER
)
""")

drivers = [
    (1, "Amit", "A", 1),
    (2, "Rahul", "B", 1),
    (3, "Priya", "C", 0),
    (4, "Neha", "D", 1),
    (5, "Rohan", "E", 1)
]

customers = [
    (101, "Deepak", "A")
]

cursor.executemany("INSERT OR REPLACE INTO drivers VALUES(?,?,?,?)", drivers)
cursor.executemany("INSERT OR REPLACE INTO customers VALUES(?,?,?)", customers)

conn.commit()
conn.close()

print("Database Created Successfully")
import sqlite3
from collections import deque


# ---------------------------
# Driver Class
# ---------------------------

class Driver:

    def __init__(self, driver_id, name, location, available):
        self.driver_id = driver_id
        self.name = name
        self.location = location
        self.available = available

    def display(self):
        print(f"""
Driver ID : {self.driver_id}
Name      : {self.name}
Location  : {self.location}
Available : {self.available}
""")


# ---------------------------
# Fetch Available Drivers
# ---------------------------

def fetch_drivers():

    conn = sqlite3.connect("ride_booking.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM drivers WHERE available=1")

    rows = cursor.fetchall()

    conn.close()

    drivers = []

    for row in rows:
        drivers.append(Driver(*row))

    return drivers


# ---------------------------
# Graph Representation
# ---------------------------

graph = {

    "A":["B","C"],
    "B":["A","D"],
    "C":["A","E"],
    "D":["B"],
    "E":["C"]

}


# ---------------------------
# BFS
# ---------------------------

def bfs(start, drivers):

    queue = deque([start])

    visited = set()

    while queue:

        city = queue.popleft()

        if city in visited:
            continue

        visited.add(city)

        for driver in drivers:

            if driver.location == city and driver.available == 1:
                return driver

        for neighbour in graph[city]:

            if neighbour not in visited:
                queue.append(neighbour)

    return None


# ---------------------------
# Assign Booking
# ---------------------------

def assign_booking(customer_id, driver):

    conn = sqlite3.connect("ride_booking.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO bookings(customer_id,driver_id) VALUES(?,?)",
        (customer_id, driver.driver_id)
    )

    cursor.execute(
        "UPDATE drivers SET available=0 WHERE driver_id=?",
        (driver.driver_id,)
    )

    conn.commit()
    conn.close()

    print("\nBooking Assigned Successfully\n")
    driver.display()


# ---------------------------
# Main
# ---------------------------

drivers = fetch_drivers()

customer_location = "A"

customer_id = 101

driver = bfs(customer_location, drivers)

if driver:
    assign_booking(customer_id, driver)
else:
    print("No Driver Available")