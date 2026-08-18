import random

# Returns a whole number (int), inclusive of both ends — so it can give you 1, 2, ... all the way up to 10. Both 1 and 10 are possible outcomes.
random_integer = random.randint(1, 10)
print(random_integer)

# Returns a float between 0.0 and 1.0 — specifically 0.0 <= x < 1.0 (never exactly 1.0). No arguments, no range you can choose — it's fixed to this 0-1 range. Example: 0.4728...
random_float_number_0_to_1 = random.random()
print(random_float_number_0_to_1)

#Same as above, just scaled up by multiplying — so now it's a float roughly between 0.0 and 10.0 (technically 0.0 <= x < 10.0).
random_float_number_0_to_10 = random.random() * 10
print(random_float_number_0_to_10)

#Returns a float directly between 1 and 10 — 1.0 <= x <= 10.0 (this one can include both endpoints, unlike random()). This is the "proper" way to get a float in a custom range — cleaner than multiplying random() yourself.
random_float = random.uniform(1, 10)
print(random_float)

#Heads and Tails
toss = random.randint(1, 2)
heads = 1
tails = 2
predict = int(input("Predict Heads or Tails? 1 or 2 :"))
if predict == toss:
    print("You win")
else:
    print("You lose")

#Choosing random string from list
l = ["Apple", "Banana", "Grapes", "Kiwi"]
ch = random.choice(l)
print(ch)