# # 2. Hospital Patient Queue Management
# ### Problem Statement
# A hospital stores patient details in SQLite.
# Each patient has:
# * Patient ID
# * Name
# * Age
# * Priority Level
# ### Requirements
# 1. Fetch all patients.
# 2. Create a **Priority Queue** based on Priority Level.
# 3. Attend patients in order of priority.
# 4. After attending a patient, update the database.
# 5. Display the remaining patients.
# ### Concepts
# * SQLite
# * Priority Queue
# * UPDATE Query
# * Heap/Priority Queue
import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    patient_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    priority INTEGER
)
""")

patients = [
    (101, "Rahul", 45, 2),
    (102, "Amit", 60, 1),
    (103, "Priya", 30, 3),
    (104, "Neha", 70, 1),
    (105, "Rohan", 25, 4)
]

cursor.executemany(
    "INSERT OR REPLACE INTO patients VALUES(?,?,?,?)",
    patients
)

conn.commit()
conn.close()

print("Database Created Successfully")