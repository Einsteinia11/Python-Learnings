# “Python is an easy-to-read, interpreted language used to build scalable applications across multiple domains.”

print("Hello World") #Hello World
print(type("hello world")) #<class 'str'>
print(type(print)) #<class 'builtin_function_or_method'>
print(type(())) #<class 'tuple'>
print(type('')) #<class 'str'>

#! Immutable -> An immutable object is one whose value cannot be changed after it is created.
#! Mutable -> A mutable object is one whose value or state can be changed after it is created.

#! Data Types
# ! 1. Numeric Types
#* int - immutable
print("Type of int: ", type(int))
a = 8
b = "0"
b = a
a = 9
print("a = ", a, "Type of a = ", type(a))
print("b = ", b, "Type of b = ", type(b))

a = "int"
print(type(type(a))) #This prints type but not considering a it is considering only type here cause the result is same for type(type())

#To Convert a = "int" to a = int without explicitly writing 
# We can do it through introspection or by dynamically access attribute

#Through introspection
a = eval(a) #not safe in production cause this can allow any user to execute any python code inside our code base
print(int ,"a = ", a, " Type of a = ", type(a))

#Through dynamic accessing attribute
# import builtins

# a = "int"
# a = getattr(builtins, a)

# print(a)        # <class 'int'>
# print(type(a))  # <class 'type'>

#* Float - immutable
a = 2.5

b = 2
print(a+b) #4.5
b = 1e309 #inf -> Max value ≈ 1.8 × 10^308
print(a + b)

#* Complex - immutable
a = 1 + 2j
b = 3j +2
print(a+b)

#! 2. Sequence types
#* String - immutable
a = "hari"
print(a)

#* List - mutable
l = [1,2,3, "fdhgf", "23"]

#* Tuple - immutable
a = ("hi", "hoi", "hi")

#* Set - mutable
a = {1,2,2,3,4,5}
print(a) #{1, 2, 3, 4, 5}

#* Range 
l = range(4) #range(0, 4)
print(l)

#! 3. Mapping Type
#* Dictionary - mutable
a = {1: "hi", 2: "hello", 3: "hoi"}

#! 4. Set Types
# * set - mutable
#* frozenset - >> Immutable
a = frozenset([1,2, 2, 2, 3])
print(a) #frozenset({1, 2, 3})

#! 5. Boolean Type
#* bool
a = True
b = False
print(a+b) #1

#! 6. Binary Types 
#* bytes - Immutable
a = b"hello"
print(a, a[0]) #b'hello' 104

#* bytearray - Mutable
a = bytearray([1, 2])
print(a, a[0]) #bytearray(b'\x01\x02') 1

#* memoryview
a = memoryview(b"abc") #<memory at 0x0000023BDD695540>
print(a)

#! 7. None
a = None

print('hello') #→ shows hello (no quotes)
#Typing 'hello' in REPL → shows 'hello' (with quotes)
#! repr
print(repr('hello\nworld')) #→ shows the string with escape characters visible
print(str('hello\nworld')) #→ shows the actual newline
a = 1
b = 1
#! id
print(id(1) == id(2)) #false - Python creates and reuses one object per integer value in that range.
print(id(a) == id(b)) #true