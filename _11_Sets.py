# Sets - A set is mutable and unorder collection of unique hashable immutable elements in python.

#! Creating empty set
s = {} #! this creates a dictionary not a set
s = set() #* Correct way
print(s) #set()

s = set((1, 2, 3)) # Convert tuple to set
print(s) #{1, 2, 3}

s = set([1, 2, 3, 5, 6]) #Convert list to set
print(s) # {1, 2, 3, 4, 5, 6}

s = set({1: "hello", 2: "bye"}) #Convert dictionaryt to set
print(s) # {1, 2}

s = set({1, "hello"}) #Convert set to set
print(s) #{1, 'hello'}

#! Python stores set elements using hashing.
#! Therefore every element inside a set must be immutable.
# s = {[1, 2, 3], {1, 2}, {1: "hello"}}
# print(s) #TypeError 
#! Set, list, dictionary not allowd

s = {1, 2, 2, 3, 2, 1}
print(s) # {1, 2, 3}

#! Immutable version of set - frozenset
fs = frozenset([1, 2, 3])
print(fs) #frozenset({1, 2, 3})

fs = frozenset({1,2,3}) #frozenset({1, 2, 3})
print(fs)

s = {1, frozenset({"hello", "bye"}), 2}
print(s) #{1, 2, frozenset({'hello', 'bye'})}

#* Boolean and integer together in set
s = {True, 0, False, 1}
print(s) #{0, True}

#! Operations
#* Add
# s.add(["hello", "Bye"]) #error
s.add("hello") 
print(s) #{0, True, 'hello'}

#* update - adds multiple values
s.update([3, 4])
print(s) #{0, True, 'hello', 3, 4}

#* remove - removes element
s.remove("hello")
print(s) #{0, True, 3, 4, 'hello'}
s.add((1, 2))
print(s) #{0, True, 3, 4, (1, 2)}
s.remove((1, 2))
print(s) #{0, True, 3, 4}
# s.remove("k") #keyerror

s.discard("k") #no error - safe remove
s.pop()
print(s) #{True, 3, 4}
s.pop()
print(s) #{3, 4}

s.clear()
print(s) #set()
s.copy() #returns shallow copy

s = {1, 2, 3}
k = s.copy()
print(s is k) #False
s.pop()
print(f"s = {s}, k = {k}") #s = {2, 3}, k = {1, 2, 3}

