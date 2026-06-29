def add(a,b):
    return a+b

def sub(a,b):
    # print(a-b)
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calc():
    num_1= int(input("Enter first number: "))
    num_2 = int(input("Enter number 2 : "))
    
    op = input("enter the operator : ")
    out_list=[]
    if op == '+':
        out = add(num_1, num_2)
        out_list.append(out)
        print(out)
    elif op =='-':
        out = sub(num_1, num_2)
        out_list.append(out)
        print(out)
    elif op =='*':
        out = mul(num_1, num_2)
        out_list.append(out)
        
        print(out)
    elif op =='/':
        out = div(num_1, num_2)
        out_list.append(out)
        
        print(out)
    else:
        print("Invalid operator")