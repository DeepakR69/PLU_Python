# # 7. Employee Attendance Analytics
# ### Problem Statement
# A company records employee attendance.
# Each record contains:
# * Employee ID
# * Name
# * Check-in Time
# * Check-out Time
# ### Requirements
# 1. Retrieve attendance records.
# 2. Calculate total working hours.
# 3. Sort employees by total hours worked.
# 4. Search employees using Employee ID.
# 5. Display employees who worked more than 45 hours this week.
# ### Concepts
# * SQL
# * Sorting
# * Binary Search
# * DateTime
import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    check_in TEXT,
    check_out TEXT
)
""")

employees = [
    (101, "Deepak", "2026-07-27 09:00", "2026-07-27 18:30"),
    (102, "Rahul", "2026-07-27 09:15", "2026-07-27 17:00"),
    (103, "Priya", "2026-07-27 08:45", "2026-07-27 18:00"),
    (104, "Amit", "2026-07-27 09:30", "2026-07-27 19:00"),
    (105, "Neha", "2026-07-27 09:00", "2026-07-27 20:00")
]

cursor.executemany(
    "INSERT OR REPLACE INTO attendance VALUES(?,?,?,?)",
    employees
)

conn.commit()
conn.close()

print("Database Created Successfully")
import sqlite3
from datetime import datetime


# -------------------------
# Employee Class
# -------------------------

class Employee:

    def __init__(self, employee_id, name, check_in, check_out):
        self.employee_id = employee_id
        self.name = name
        self.check_in = check_in
        self.check_out = check_out
        self.total_hours = self.calculate_hours()

    def calculate_hours(self):

        start = datetime.strptime(self.check_in, "%Y-%m-%d %H:%M")
        end = datetime.strptime(self.check_out, "%Y-%m-%d %H:%M")

        hours = (end - start).total_seconds() / 3600

        return round(hours, 2)

    def display(self):
        print(f"""
Employee ID : {self.employee_id}
Name        : {self.name}
Check In    : {self.check_in}
Check Out   : {self.check_out}
Hours       : {self.total_hours}
""")


# -------------------------
# Fetch Records
# -------------------------

def fetch_records():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    rows = cursor.fetchall()

    conn.close()

    employees = []

    for row in rows:
        employees.append(Employee(*row))

    return employees


# -------------------------
# Binary Search
# -------------------------

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid].employee_id == target:
            return arr[mid]

        elif arr[mid].employee_id < target:
            left = mid + 1

        else:
            right = mid - 1

    return None


# -------------------------
# Main Program
# -------------------------

employees = fetch_records()

# Sort by Total Hours
employees.sort(key=lambda x: x.total_hours, reverse=True)

print("\nEmployees Sorted by Working Hours\n")

for emp in employees:
    emp.display()


# Binary Search
employees.sort(key=lambda x: x.employee_id)

eid = int(input("\nEnter Employee ID to Search: "))

result = binary_search(employees, eid)

if result:
    print("\nEmployee Found")
    result.display()
else:
    print("Employee Not Found")


# Employees worked more than 45 hours
print("\nEmployees who worked more than 45 hours this week\n")

found = False

for emp in employees:

    weekly_hours = emp.total_hours * 5      # Assuming 5 working days

    if weekly_hours > 45:
        emp.display()
        found = True

if not found:
    print("No employee worked more than 45 hours.")
