# # 

# GLOBAL_VAR = 10

# def function_one(a):
#     b = 9
#     print( GLOBAL_VAR * a+ b)
    
# def function_two(x):
#     y = 88
#     print( GLOBAL_VAR * x+ y)

'''
OOPs : Object Oriented Programming

'''

class ClassOne:
    # def __init__(self, Name):
    #     self.classonename = Name
    
    ClassOnename = "Class One"
        
class ClassTwo(ClassOne):
    def __init__(self, Name):
        self.classtwoname = Name
        
class ClassThree:
    def __init__(self, Name):
        self.classthreename = Name
        
        
obj = ClassTwo("ClassTwo")
print(obj.ClassOnename)