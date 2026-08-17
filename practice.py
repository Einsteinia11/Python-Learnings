import builtins
import copy
#* Enter list through user input using append
# n = int(input("Enter range for list: "))
# l = []
# for j in range(0, n):
#     i = input(f"Enter value at {j} index: ")
#     l.append(i)
# print(l)

#* Enter list through user input using insert
# n = int(input("Enter range for list: "))
# l = []
# for j in range(0, n):
#     i = input(f"Enter value at {j} index: ")
#     l.insert(j, i)
# print(l)

#* Enter list through user input using extend
# n = int(input("Enter range for list: "))
# l = [2]
# for j in range(0, n):
#     i = input(f"Enter value at {j} index: ")
#     l.extend(j)  #TypeError: 'int' object is not iterable
# print(l)

# Python executes:
# l.extend(0)
# But extend() expects something like:
# l.extend([0])
# l.extend((0,))
# l.extend("abc")

#* Convert string into code
a = "int"
b = getattr(builtins, a)
print(b)

# Find position of what user is searching in list
# l = ["apple", "football", "book a", "spoon", "rope"]
# s = input("Enter the searching item: ")
# try:
#     i = l.index(s)
#     print(i)
# except ValueError:
#     print("Value not found")

#Ternery operator
happy = True
s = "True" if happy == True else "False"
print(s)

#List comprehension
odd = [i for i in range(0, 20) if i%2==1]
evenodd = [f"{i} is even" if i%2==0 else f"{i} is odd" for i in range(0, 20)]
print(odd)
print(evenodd)

#Finding a character or word in string
# ch = input("Enter to find out: ")
# s = "hey there what's up? Here you will find answers of anything."
# print("Found at index ", s.find(ch))
# try:
#     print(s.index(ch))
# except ValueError:
#     print("Not found")

# shallow copy and reference copy

a = 2
b = a
print("a is b = ", a is b, " b is a = ", b is a)

a = "huhf"
c = copy.copy(a)
print("a is c = ", a is c, " c is a = ", c is a) #true for both - why? - Strings are immutable. Since they cannot be modified, copy.copy() doesn't create a new string object. It simply returns the original object.
a = 2
d = copy.copy(a)
print("a is d = ", a is d, " d is a = ", d is a) #again true true - why? - Because a is an integer, and integers are immutable in Python.

a = [1, 2, 3]
b = copy.copy(a)
print(a is b) #false - For mutable objects like lists, dictionaries, and sets it creates a new container object

