# 3. Arrange Exam Marks
# A teacher wants to display students' marks from the lowest to the
# highest.
# Write a program to sort the marks of all students in ascending orde

def bubble_sort(marks):
    n = len(marks)

    for i in range(n - 1):              # number of passes
        swapped = False

        for j in range(n - 1 - i):     # shrinks each pass (last i elements already sorted)
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]   # swap
                swapped = True

        if not swapped:                 # list already sorted — stop early
            break

    return marks

n = int(input("Enter number of students: "))

marks = []
for i in range(n):
    m = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(m)

print("\nMarks before sorting:", marks)

bubble_sort(marks)

print("Marks after sorting (lowest to highest):", marks)