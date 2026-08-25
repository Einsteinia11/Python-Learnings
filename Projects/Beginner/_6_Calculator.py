def add(a, b):
    return a+b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
def show_result(res, op):
    if op == 1:
        op = "Addition"
    elif op == 2:
        op = "Subtraction"
    elif op == 3:
        op = "Multiplication"
    elif op == 4:
        op = "Division"
    print(f"The result for {op} is {res}")
def callfunction(a, b, op):
    if op == 1:
        return show_result(add(a, b), op)
    elif op == 2:
        return show_result(subtract(a, b), op)
    elif op == 3:
        return show_result(multiply(a, b), op)
    elif op == 4:
        return show_result(divide(a, b), op)
    else:
        print("Wrong Choice!, Please enter operation from the shown items")
y = "y"
while y == "y":
    print("""
    Press the listed numbers for performing operations
    Addition - 1
    Subtraction - 2
    Multiply - 3
    Division - 4
    """)
    op = int(input("Enter operation:"))
    a = int(input("Enter first digit:"))
    b = int(input("Enter second digit:"))
    callfunction(a, b, op)
    y = input("Enter y to continue else press any other key")
