#  Handle division by zero using try and except
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")