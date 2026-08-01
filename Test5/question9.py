# # 9. Library Book Borrowing System
# ### Problem Statement
# A library stores books and borrowing history.
# Tables:
# Books
# Members
# Borrowed Books
# ### Requirements
# 1. Display all available books.
# 2. Sort books alphabetically using **Merge Sort**.
# 3. Search books by Book ID.
# 4. Borrow a book.
# 5. Update book availability.
# 6. Display overdue books.
# ### Concepts
# * Merge Sort
# * Binary Search
# * SQLite
# * SQL UPDATE
import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    available INTEGER
)
""")

# Members Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS members(
    member_id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Borrowed Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS borrowed_books(
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER,
    book_id INTEGER,
    borrow_date TEXT,
    due_date TEXT,
    returned INTEGER
)
""")

books = [
    (101,"Python Programming","Guido",1),
    (102,"Data Structures","Mark",1),
    (103,"Operating System","Galvin",0),
    (104,"Database System","Korth",1),
    (105,"Machine Learning","Tom",1)
]

members = [
    (1,"Deepak"),
    (2,"Rahul")
]

borrowed = [
    (1,103,"2026-07-01","2026-07-15",0)
]

cursor.executemany("INSERT OR REPLACE INTO books VALUES(?,?,?,?)",books)
cursor.executemany("INSERT OR REPLACE INTO members VALUES(?,?)",members)
cursor.executemany("""
INSERT OR REPLACE INTO borrowed_books
(member_id,book_id,borrow_date,due_date,returned)
VALUES(?,?,?,?,?)
""",borrowed)

conn.commit()
conn.close()

print("Database Created Successfully")
import sqlite3
from datetime import datetime


# ------------------------
# Book Class
# ------------------------

class Book:

    def __init__(self, book_id, title, author, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display(self):
        print(f"""
Book ID    : {self.book_id}
Title      : {self.title}
Author     : {self.author}
Available  : {"Yes" if self.available else "No"}
""")


# ------------------------
# Fetch Available Books
# ------------------------

def fetch_books():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE available=1")

    rows = cursor.fetchall()

    conn.close()

    books=[]

    for row in rows:
        books.append(Book(*row))

    return books


# ------------------------
# Merge Sort
# ------------------------

def merge_sort(arr):

    if len(arr)<=1:
        return arr

    mid=len(arr)//2

    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    return merge(left,right)


def merge(left,right):

    result=[]

    i=j=0

    while i<len(left) and j<len(right):

        if left[i].title.lower()<right[j].title.lower():
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ------------------------
# Binary Search
# ------------------------

def binary_search(arr,target):

    left=0
    right=len(arr)-1

    while left<=right:

        mid=(left+right)//2

        if arr[mid].book_id==target:
            return arr[mid]

        elif arr[mid].book_id<target:
            left=mid+1

        else:
            right=mid-1

    return None


# ------------------------
# Borrow Book
# ------------------------

def borrow_book(member_id,book_id):

    conn=sqlite3.connect("library.db")
    cursor=conn.cursor()

    today=datetime.today().strftime("%Y-%m-%d")

    due="2026-08-05"

    cursor.execute("""
    INSERT INTO borrowed_books
    (member_id,book_id,borrow_date,due_date,returned)
    VALUES(?,?,?,?,?)
    """,(member_id,book_id,today,due,0))

    cursor.execute("""
    UPDATE books
    SET available=0
    WHERE book_id=?
    """,(book_id,))

    conn.commit()
    conn.close()

    print("Book Borrowed Successfully")


# ------------------------
# Display Overdue Books
# ------------------------

def overdue_books():

    conn=sqlite3.connect("library.db")
    cursor=conn.cursor()

    today=datetime.today().strftime("%Y-%m-%d")

    cursor.execute("""
    SELECT books.book_id,
           books.title,
           borrowed_books.due_date
    FROM books
    JOIN borrowed_books
    ON books.book_id=borrowed_books.book_id
    WHERE borrowed_books.returned=0
    AND borrowed_books.due_date<?
    """,(today,))

    rows=cursor.fetchall()

    conn.close()

    print("\nOverdue Books\n")

    if len(rows)==0:
        print("No overdue books.")
    else:
        for row in rows:
            print(row)


# ------------------------
# Main
# ------------------------

books=fetch_books()

books=merge_sort(books)

print("\nAvailable Books\n")

for book in books:
    book.display()

books.sort(key=lambda x:x.book_id)

bid=int(input("Enter Book ID: "))

book=binary_search(books,bid)

if book:
    print("\nBook Found")
    book.display()
else:
    print("Book Not Found")

member=int(input("\nEnter Member ID: "))

borrow_book(member,bid)

overdue_books()