# Functions - A function in python is a reusable block of code which performs a specific task and can optionally accept input or return some output.
def foo():
    return
print(foo()) #None

# def foo(a=0, b): #Syntaxerror correct: a, b
    # b = 0
    # pass
# print(foo(b=2)) #None

def add():
    print(10+20)

print(add())#30 None
result = add()
print(result)

def add(a, b):
    return a+b
add(a = 2, b = 3) #doesnot prints the value

def foo(a, b):
    s = a+b
    m = a*b
    d = a/b
    return s, m, d #Python returns multiple values packed in a tuple it is same as (s, m, d)
#unpacking
a, b, c = foo(a = 3, b = 4)
print(f"a = {a}, b = {b}, c = {c}") #a = 7, b = 12, c = 0.75

def add_item(a = 1, l = []):
    l.append(2)
    print(l) #[2]
add_item(a = 2, l = [])

def add_item(a = 0, l = []): #Mutable defaults are shared between function calls.
    l.append(a)
    print(l) #[2]
add_item(a = 2) 
add_item(a = 3) # [2, 3]
add_item(a = 4) #[2, 3, 4] 

def add_item(item, lst=None):
    if lst is None:
        lst = []

    lst.append(item)
    print(lst)
add_item(2) #[2]
add_item(4) #[4]
add_item(5) #[5]

