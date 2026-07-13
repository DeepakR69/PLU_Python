
# Create a Student class with name and age, then display them.
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s = Student("Deepak", 22)
s.display()