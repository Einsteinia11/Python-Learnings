# Tuples - A tuple is an ordered and immutable sequence type in Python used to store multiple values together.

#"A tuple is an ordered, immutable collection in Python used to store multiple values. It supports indexing, slicing, packing, unpacking, and can contain heterogeneous data types. Since tuples are immutable, their elements cannot be modified after creation."

#! Creating Tuples
#* 1. Direct create
t = (10, 20, 30)
print(t)

#* 2. Without Parentheses
t = 10, 20, 30
print(t)

#* Using tuple constructor
t = tuple([10, 20, 30])
print(t)

#! Creating tuple from user input
#* String input
# s = input("Enter values separated by spaces: ")
# t = tuple(s.split())
# print(t)

#* integer input
# s = tuple(map(int, input("Enter values separated by spaces: ").split()))
# print(s)

#! Using LIst comprehension 
# t = tuple([int(input(f"Enter value at {i} index : ")) for i in range(0, 4)])
# print(t)

#! Single element tuple
#!Wrong
t = (10)
print(type(t)) #int
#*Correct
t = (10,)
print(type(t)) #tuple

#! Accessing tuple elements
t = ("hello", 10, 20, 30)
print(t[0])
print(t[1])

#! Negative indexing
print(t[-1])

#! Slicing
print(t[1:4])

#! Modifying a Tuple
# t[0] = "hello" #TypeError

#* Convert to list
temp = list(t)
temp[0] = 100
t = tuple(temp)
print(t)

#* Reassign entire tuple
t = (200, 30, 40)

#* Concatenation
t+=(3,)
print(t)

#! Mutable Objects inside Tuple
t = (10, 20, [1, 2, 3], 40)
t[2].append(4)
print(t)

#! Tuple unpacking
a, b, c, d = t
print(c)
c[0] = 10
print(t)

#! Important - This doesn't creates tuples
t = (i for i in range(0, 5)) #It creates a generator object
print(type(t)) #<class 'generator'>

#! Create Tuple using Generator expression
t = tuple(i for i in range(0, 5))

#! Tuple has only two builtin method
#* count()
t = (10, 20, 10, 10, 10)
print(t.count(10)) #4

#* index()
print(t.index(10)) #0

