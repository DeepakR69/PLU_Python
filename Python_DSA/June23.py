'''
Data Type : 
    - Numeric 
    - Sequence : string, list, tuple, range()
    - Set : set, frozenset
    - Mapping : dictionary
    - Boolean : Ture and False


Operators : 
    - Arithmetic : +, -, *, /, %, //, **
    - Assignment : =, +=, -=, *=, /=, %=
    - Comparison : ==, !=, >, <, >=, <=
    - Logical : and, or, not
    - bitwise : &, |, ~, ^
    - Identity : is, is not
    - Membership : in, not in
    
Control Flow : 
    - conditional statements 
        - if 
    - loop 
        - for 
        - while 

Functions :     

def function_name(parameters or arguments):
    statements
    
    retrun statement
    
    
Arguments :     Default, keyword, *args, **kwargs

Type of function :
    - Built in 
    - user defined
    - lambda or anonymous
    - Higher order functions : 
        - Generator functions
        - Decorator functions
        
File Handling: 
    1 . opening a file  : open('file_name', 'mode')
    2 . operation on file : read read(), write, append write()
    3 . closing a file : close()
    
modes : 
    r , w , a
    r+, w+, a+
    rb, wb, ab 
    rb+, wb+, ab+
    
    x
    
WE ARE NOT HANDLING THE ERROR BUT HANDLING THE TERMINATION STATE OF THE APP

'''
try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))

except:
    print( "some error")