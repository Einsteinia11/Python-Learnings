import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '+', '=', '[', ']',
    '{', '}', '|', '\\', ':', ';', '"', "'",
    '<', '>', ',', '.', '?', '/'
]
password = []
print("This is a Password Generatpr program")
l = int(input("Enter how many letters you want: "))
n = int(input("Enter how many numbers you want: "))
s = int(input("Enter how many symbols you want: "))

for i in range(0, l):
    password.append(random.choice(letters))
for i in range(0, n):
    password.append(random.choice(numbers))
for j in range(0, s):
    password.append(random.choice(symbols))

passw = ""
for i in password:
    passw+=i
print(passw)