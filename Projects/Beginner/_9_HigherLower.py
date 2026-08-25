from Fonts.HigherLowerFont import font
from Data.Celebrities import celebrities
l = []
score = 0
def start():
    print("Welcome to the")
    print(font)
    print("GAME.")

def ask_question(ran):
    global l
    r = ran +1
    if r < len(celebrities):
        for i in range(ran, r):
            l.append(celebrities[i])
            print(l[i]["name"])
    compare()

def win(a):
    global score
    global y
    score +=1
    print(
        f"""
        ════════════════════════════════════════════════

                    🎉 CORRECT! 🎉

                    {a} has MORE followers!

                        SCORE: {score}
        ════════════════════════════════════════════════
        """
    )
    y = "y"

def lose(a):
    global score
    global y
    score -=1
    print(
            f"""
            ════════════════════════════════════════════════
    
                        🎉 You loss! 🎉
    
                        {a} has MORE followers!
    
                            SCORE: {score}
            ════════════════════════════════════════════════
            """
        )
    y = "s"

def compare():
    print(f"""
               ════════════════════════════════════════════════
        
                                WHO HAS MORE?
        
                            ⭐ {l[-2]["name"]}
                                Famous for: {l[-2]["famousfor"]}
        
                                Followers: {l[-2]["followers"]}
        
                                            VS
        
                            ⭐ {l[-1]["name"]}
                                Famous for: {l[-1]["famousfor"]}
        
                                Followers: ???
        
                ════════════════════════════════════════════════
        
                [A] {l[-2]["name"]}
                [B] {l[-1]["name"]}
        
                Who has more followers?
                """)
    ask = input("Write here [a] or [b]: ")
    a = l[-2]["followers"]
    b = l[-1]["followers"]
    if ask == "a" and a>b:
        print("1st condition")
        win(l[-2]["name"])
    elif ask == "b" and b>a:
        print("2 condition")
        win(l[-1]["name"])
    elif ask == "a" and b>a:
        print("3 condition")
        lose({l[-1]["name"]})
    elif ask == "b" and a>b:
        print("4 condition")
        lose(l[-2]["name"])
    elif (ask == "a" or ask == "b") and a==b:
        print("5 condition")
        win(l[-2]["name"])
    else:
        print("Invalid response")

y = "y"
while y == "y":
    start()
    score = 0
    count = 0
    l.append(celebrities[0])
    ask = "y"
    while ask == "y":
        count += 1
        ask_question(count)
        if y == "s":
            ask = input("Enter y to start else press any other key")
            y = "s"
    
