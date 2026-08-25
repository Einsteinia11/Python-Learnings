import random
print("🎮 WELCOME TO HANGMAN! 🎮")

print("Guess the hidden word, one letter at a time.")

print("You have 3 lives ❤️")
print("Guess carefully!")

print("Let's begin... 🔤")
words = [
    "python", "computer","programming","developer","keyboard","internet","elephant","giraffe","tiger","penguin","rainbow",
]
word = random.choice(words)
letter = random.choice(word)
c = ""
life = 3
for i in word:
    if i != letter:
        c+=i
    else:
        c+="_"
print(c)
while life>0:
    l = input("Enter letter: ")
    if l == letter:
        print("""✅ Great guess!
You found a letter! 🎉""")
        break
    else:
        life-=1
        print("Wrong guess you lost a life! 💔")
        if (life == 2):
            print("""
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========""")
        elif (life == 1):
            print("""
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========""")
        else:
            print("Oops You lost")
            print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")
