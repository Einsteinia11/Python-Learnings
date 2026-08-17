#* Arithmetic Operators 

# +, -, *, /, //, %, **

#* Floor Division - // (✔ Removes decimal part)
a = 11
b = 2
print("Floor division: 11//2 = ", a//b)

#* Modulus - % (✔ Gives remainder)
print("Modulus a%b = ", a%b)

#* Power - **
print("Power a**b = ", a**b)

#* Assignment Operators

# =, +=, -=, *=, /=

balance=1000
balance+=500   # deposit
balance-=200   # withdraw

#* Comparison Operators

# ==, !=, >, <, >=, <=

age=20
print(age>=18)

a= [1,2]
b= [1,2]

print(a==b) #Checks value
print(a is b) #Checks Memory

#* Logical Operators
# and, or, not

age=20
citizen=True
print(age>=18 and citizen)

#* Identity Operators
# is, is not

a= [1,2]
b=a
print(a is b)

#* Membership Operators
skills= ["Python","SQL"]
print("Python" in skills)

#Dealing with negative numbers
print(-3/-2) #1.5
print(-3/2)  #-1.5
print(3/-2)  #-1.5
print(-3//2) #-2
print(-3//-2) #1
print(-6%4) #2
print(-0) #0
print(True is 1)