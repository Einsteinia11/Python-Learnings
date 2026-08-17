#print
print("Hello World")

#Multiple Values
name = "Kajal"
age = 22

print("Name:", name, "Age:", age)

#f-string
print(f"My name is {name}")

#Formatting
print("Hello", end=" ")
print("World")

#input
age = input("Enter age: ")
# print(age + 5)   # Error

age = int(input("Enter age: "))
print(age + 5)

#Multiple Inputs in One Line
a, b = map(int, input("Enter two numbers: ").split())

print(a + b)

#Taking list input
nums = list(map(int, input("Enter numbers: ").split()))
print(nums)

#eval() evaluates a string as a Python expression.
x = eval(input("Enter value: "))

# Using list comprehension
nums = [int(x) for x in input().split()]

#using map
nums = list(map(int, input().split()))
