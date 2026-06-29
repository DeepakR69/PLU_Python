# '''
# Physical & Logical Objects
# Class
# class_variable
# . operator
# ___init___()
# self 
# methods 
# object
# Encapsulation
# Inheritance

# Scope & Namespace
# '''

# def abc(a,b):
#     pass

# abc(1,2)
# def abc(a,b,c):
#     pass

# abc(1,2,3)


from abc import ABC

## our Abstract Class
class classOne(ABC):
    def display(self):
        pass

class classTwo(classOne):
    def display(self):
        print("This is Class Two")