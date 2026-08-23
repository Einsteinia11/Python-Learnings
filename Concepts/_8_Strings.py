#Single Quotes
s = 'hello'

#! Double quotes
s = "Hi"

#! Triple Quotes
s = """This 
is a 
multiline 
string"""

#! String Indexing
print(s)
print(s[1])
print(s[2])

#! String Slicing
# s[start:end:step]
print(s[0:10:1])
print(s[::2])

#Reverse String
print(s[::-1])

#! String Immutability
s = "Python"
# s[0] = "K" #Typeerror

#! Case Conversion methods
s = s.upper() #PYTHON
print(s)
s = s.lower() #python
print(s)
s = s.title() #Python
print(s)
s = s.capitalize() #Python
print(s)

#* Differnce between title and capitalize is capitalize converts first character of the entire string to upperccase and title converts first character of every word to uppercase

#! Whitespace Methods
s = "  pyThon   "
s = s.rstrip() # Remove right spaces
print(s)
s = s.lstrip() # Remove left spaces
print(s)
s = "  pyThon   "
s = s.strip() # Remove spaces both sides
print(s)

#! Search Methods
# Finds Index of the given character
print(s.find("T")) #2 if character not found returns -1

#index
print(s.index("T")) #2 similar to find

#* difference b/w index and find is find returns -1 if not found and index raises error

#count occurrences
s = "pppppppppythonpp"
print(s.count("p")) #11

#check start
print(s.startswith("p")) #True

#check end
print(s.endswith("n")) #False

#! Replace
s = "I like Roses."
print(s.replace("Roses", "Dandelion"))
s = s.replace("I like Roses.", "I like Dandelions.")
print(s)

#! Split & Join
# split() - Converts string to list
s = s.split()
print(s) #['I', 'like', 'Dandelions.']

#join() - Converts list to string
s = " ".join(s) #I like Dandelions.
print(s)

#!String Formatting
#f-strings
s = "Dandelions"
print(f"I like {s}.") #I like Dandelions.

#format()
print("I like {}.".format(s)) #I like Dandelions.

#! Escape Characters
#\n - new line
# \t	Tab
# \\	Backslash
# \"	Double quote
print("\tI \n\tlove \"\n\tscriptures\"")

