
# 7. Create student.txt, write your name, then read and display it.
file = open("student.txt", "w")
file.write("Deepak Ruhela")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()