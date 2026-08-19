import random

rock = 1
paper = 2
scissors = 3
n = int(input("Enter 1 for rock 2 for paper 3 for scissors: "))
c = random.randint(1, 3)
print("You = ", n, " Computer = ", c)
if (c == rock and n == 1) or (c == paper and n == 2) or (c==scissors and n == 3):
    print("Match Draw as both are same")
elif c == rock and (n == 2 or n == 3):
    print("Computer won by rock")
elif c == paper and (n == 1 or n == 3):
    print("You won as computer thrown paper")
elif c == scissors and n == 1:
    print("You won as computer thrown scissors over rock")
elif c == scissors and n == 2:
    print("Computer won by throwing scissors over paper")
    