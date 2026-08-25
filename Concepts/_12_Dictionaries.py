# Dictionaries

# Empty Dictionary
d = {}
d = dict()

# Dictionary with values
K = {
    "Name" : "Kajal Lanjhiyana",
    "Age" : 22
}

# Dictionary using Dict
K = dict(name = "Kajal Lanjhiyana", age = 22)

#Dictionary with mixed values
D = {
    "name": "Kajal",
    "Age" : 22,
    "Grade": 70,
    "Alive": True,
    "Species": "Human Being",
    "Hobbies": ["Coding", "Singing", "Dancing", "Writing"]
}

#Dictionary Comprehension
l = ["apple", None, "pomogranate", "kivi"]
d = {i: l[i] for i in range(0, len(l))}
print(d)

# Dictionary Methods
#! d.get
print(d.get(1, "Strawberry")) #None
print(d.get(4, "Strawberry")) #Strawberry"

#! d.keys
print(d.keys()) #dict_keys([0, 1, 2, 3])

#! d.values
print(d.values()) #dict_values(['apple', None, 'pomogranate', 'kivi'])

#! d.items
print(d.items()) #dict_items([(0, 'apple'), (1, None), (2, 'pomogranate'), (3, 'kivi')])

#! d.update
print(d.update({4: "orange"})) #NOne
print(d)
#! d.pop
# print(d.pop())

#! Keys in dictionary are stored using hashing - That's why dictionary lookups are easy
# d = {[1, 2]: "hello"} #error - list is mutable so can't be used as key cause mutable objects can change their hash values 
d = {(1, 2): "tuple", "2": "string", 3.5: "float", frozenset({1, 2}): "hi"}

#! Membership checks keys only
print((1, 2) in d)

#counting frequency of character occurred in list 
l = ["apple", "mango", "berry", "strawberry"]
freq = {}
for i in l:
    for j in i:
        freq[j] = freq.get(j, 0) + 1
print(freq)

#! looping through dictionaries
l = {1: "hello", 2: "hi", 3: "hola", 4: "hui"}

#* through keys
print("Looping through keys")
for i in l:
    print(i, end = " ") #1 2 3 4
print(" ")

#* through keys and values
print("Looping through keys and values")
for i, j in l.items():
    print(i, j, end = " ") #1 hello 2 hi 3 hola 4 hui
print()

for i, j in enumerate(l.items()):
    print(i, j, end = " ") # 0 (1, 'hello') 1 (2, 'hi') 2 (3, 'hola') 3 (4, 'hui') 
print()
print("###################")
j = {
    "a" : {
        "b": "c",
        "d": "e", 
    },
    "f": {
        "b" : "h",
        "i" : "j"
    }
}
# for i in j.keys():
#     print(i["b"]) #TypeError: string indices must be integers, not 'str'

for i, k in j.items():
    print(i, k["b"])