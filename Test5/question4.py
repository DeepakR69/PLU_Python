
# ---
# # 4. College Placement Portal
# ### Problem Statement
# A college stores student records in SQLite.
# Each student contains:
# * Roll Number
# * Name
# * CGPA
# * Skills
# * Placement Status
# ### Requirements
# 1. Retrieve all students.
# 2. Sort students by CGPA using **Heap Sort**.
# 3. Search students by Roll Number.
# 4. Display students eligible for placements (CGPA > 7.5).
# 5. Update placement status after selection.
# ### Concepts
# * Heap
# * Heap Sort
# * Binary Search
# * SQL UPDATE
import sqlite3

conn = sqlite3.connect("placement.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    cgpa REAL,
    skills TEXT,
    placement_status TEXT
)
""")

students = [
    (101, "Deepak", 8.6, "Python, SQL", "Not Placed"),
    (102, "Rahul", 7.2, "Java", "Not Placed"),
    (103, "Priya", 9.1, "Python, AI", "Not Placed"),
    (104, "Amit", 6.9, "C++", "Not Placed"),
    (105, "Neha", 8.0, "Java, SQL", "Not Placed")
]

cursor.executemany(
    "INSERT OR REPLACE INTO students VALUES(?,?,?,?,?)",
    students
)

conn.commit()
conn.close()

print("Database Created Successfully")