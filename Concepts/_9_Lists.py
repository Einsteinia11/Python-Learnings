#Creating lists
l = []
#Mixed data types nested list
l = ["1", "hello", 2, {1: "hi", 2: "Hello"}, [1,2,3,4], (1,2), {1,2,3}]

#! List indexing
print(l[4]) #[1, 2, 3, 4]

#! Negative Indexing
print(l[-3]) #[1, 2, 3, 4]

#! List Slicing
print(l[1: -1: 2]) #['hello', {1: 'hi', 2: 'Hello'}, (1, 2)]

print(l[::3]) #['1', {1: 'hi', 2: 'Hello'}, {1, 2, 3}]

#! List Mutability
l[0] = [1,23]

#! List Methods
#* Append
l.append("hoi")

#* Extend
l.extend([1,2,3, "at the end"])

#* Insert
l.insert(1,100)
print(l) #[[1, 23], 100, 'hello', 2, {1: 'hi', 2: 'Hello'}, [1, 2, 3, 4], (1, 2), {1, 2, 3}, 'hoi', 1, 2, 3, 'at the end']

#! Remove Elements
#* remove - removes through value
l.remove(3)

#*pop - Removes from index
l.pop(0)
l.pop(2)
l.pop() #Removes last index

#! Searching Methods
#*index
print(l.index("hello")) #Find position
print(l.count(2)) #Counts occurrences

#! Sorting Methods
#* sort()
l2 = [1,99,0,4,7]
print(l2.sort()) #None
print(l2) #[0, 1, 4, 7, 99]

#* reverse
l2.reverse()
print(l2)

#! List Comprehension
#* List comprehension with condition
# [expression for item in iterable if condition]
evens = [i for i in range(0, 10) if i%2==0]
for i in evens:
    print(i, end = " ") #0 2 4 6 8 

#* Conditional expression
# [true_value if condition else false_value for item in iterable]
evens = [i if i%2==0 else f"{i} is odd" for i in range(0, 10)]
for i in evens:
    print(i) #0 2 4 6 8 
