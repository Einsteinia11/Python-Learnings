#range(start, stop, step) - generates a sequence of numbers.

#! range(stop)
print(range(5)) #range(0, 5)
a = range(5)
for i in a:
    print(i, end = " ") #0 1 2 3 4
print()

#! Iteration
l = [1,2,3,4,5]
it = iter(l)
print(it) #<list_iterator object at 0x000001E7D1F905B0>
print(next(it)) #1
print(next(it)) #2

#! For loop
for i in range(0, 4):
    print("*", end = " ")
print()

#! Step in for loop
for i in range(0, 12, 2):
    print(i, end = " ")
print()

#! while loop
i = 0
while i in a:
    print(i, end = " * ") #0 * 1 * 2 * 3 * 4 *
    i+=1 

#! Loop control Statements
for i in range(0, 12):
    if i%2 == 1:
        print("i = ", i)
        continue #Skip current iteration
    print("i = ", i)
    print("I will not be executed if it is an odd number.")
    if i == 10:
        print("I stopped the execution at 10 due to sudden break")
        break #Exit loop immediately
    if i == 11:
        pass #Placeholder statement

#! Loop else
# The else block executes when the loop completes normally without break.
#* without break
for i in range(0, 3):
    if i == 3:
        break
else:
    print("For loop executed without break")

#* without break
for i in range(0, 3):
    if i == 1:
        print("For loop executed without else")
        break
else:
    print("For loop executed without break")

#! Nested Loops
for i in range(0, 9):
    for j in range(0, i):
        print("*", end = " ")
    print("")

#! Zip
a = ["Hari", "Radhe"]
b = ["Bol", "Krishna"]
for i, j in zip(a, b):
    print(i, j)

