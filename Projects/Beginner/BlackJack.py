import random
print("""
                            ╔══════════════════════════════════════════╗
                            ║            ♠ BLACKJACK ♠                 ║
                            ║         THE 21 CARD GAME                 ║
                            ╚══════════════════════════════════════════╝
""")
user1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6 ,7, 7, 8, 8, 9, 9, 10, 10, "A", "Q", "J", "K"]
user2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6 ,7, 7, 8, 8, 9, 9, 10, 10, "A", "Q", "J", "K"]
user1_cards = []
user2_cards = []
game = "c"
def check(a, user):
    if a == "A":
        if sum(user) > 11:
            a = 1
        else:
            a = 11
    elif a == "Q" or a == "J" or a == "K":
        a = 10
    # print("a = ", a)
    return a

def start():
    def set_cards(user, deck):
        for i in range(0, 2):
            r = random.choice(deck)
            # print("r = ", r)
            if r == "A" or r == "Q" or r == "K" or r == "J":
                # print("r = ", r)
                deck.remove(r)
                # print("check(r, user)", check(r, user))
                user.append(check(r, user))
                
            else:
                deck.remove(r)
                user.append(r)
    set_cards(user1_cards, user1)
    set_cards(user2_cards, user2)
    # print("user1 crads = ",user1_cards)
    # print("user2 crads = ",user2_cards)
    # print("user1 crads = ",user1)
    # print("user2 crads = ",user2)
    print(f"""
            ────────────────────────────────────────────
                        🎲 NEW ROUND
            ────────────────────────────────────────────

            Dealer is shuffling the deck...
            Dealing cards...

            Your cards:                                      Opponent's cards:
            ┌──────┐                      ┌───────┐
               {user1_cards[0]}                              {user2_cards[0]}   
               {user1_cards[1]}                              -    
            └──────┘                      └───────┘

            Your total: {sum(user1_cards)}
    """)
    
def hit(user):
    r = random.choice(user)
    user.remove(r)
    print("user = ", user)
    if user == user1:
        user1_cards.append(check(r, user1_cards))
        print(f"""
            You chose: HIT

            Dealing a card...

            You received: {r}
            
            Your Total: {sum(user1_cards)}
        """)
        print("Your cards: ",user1_cards)
    else:
        print("Dealer choose Hit he got something good card now it's your turn")
        user2_cards.append(check(r, user2_cards))
    return r
def check_bust():
    global game
    if sum(user1_cards)>21 and sum(user2_cards)<=21:
        print(f"""
        ────────────────────────────────────────────
                        💥 BUST!
        ────────────────────────────────────────────

            Your total: {sum(user1_cards)}

            Dealer total: {sum(user2_cards)}

                      Dealer Wins!
        ────────────────────────────────────────────
        """)
        game = "s"
    elif sum(user1_cards)<=21 and sum(user2_cards)>21:
            print(f"""
            ────────────────────────────────────────────
                            💥 BUST!
            ────────────────────────────────────────────
    
                Your total: {sum(user1_cards)}
    
                Dealer total: {sum(user2_cards)}
    
                         You Win!
            ────────────────────────────────────────────
            """)
            game = "s"
        
    elif sum(user2_cards)>21 and sum(user1_cards)<=21:
        print(f"""
                ╔══════════════════════════════════════════╗
                ║              YOU WIN! 🎉                 ║
                ╚══════════════════════════════════════════╝

                Your total:   {sum(user1_cards)}
                Dealer total: {sum(user2_cards)}

                The house couldn't beat you!
        """)
        game = "s"
        

def stand():
    global game
    if sum(user2_cards)<17:
        check_bust()
        hit(user2)
    else:
        if sum(user1_cards) > sum(user2_cards):
            game = "s"
            print(f"""
                ╔══════════════════════════════════════════╗
                ║              YOU WIN! 🎉                 ║
                ╚══════════════════════════════════════════╝

                Your total:   {sum(user1_cards)}
                Dealer total: {sum(user2_cards)}

                The house couldn't beat you!
            """)
        elif sum(user1_cards) == sum(user2_cards):
            print("""
                ────────────────────────────────────────────
                                PUSH 🤝
                ────────────────────────────────────────────

                Your total:   20
                Dealer total: 20

                It's a tie!
                Your bet is returned.
                ────────────────────────────────────────────
            """)
            game = "s"
            
        elif sum(user1_cards) < sum(user2_cards):
            print(f"""
                ────────────────────────────────────────────
                                💥 You Loose!
                ────────────────────────────────────────────

                Your total: {sum(user1_cards)}

                Dealer total: {sum(user2_cards)}

                            DEALER WINS
                ────────────────────────────────────────────
            """)
            game = "s"
        else:
            game = "c"
            
def Dealer():
    ch = ["hit", "stand"]
    if sum(user2_cards) < 17:
        hit(user2)
    elif 21>=sum(user2_cards) > 17:
        r = random.choice(ch)
        if r == "hit":
            hit(user2)
        elif r == "stand":
            stand()
    else:
        check_bust()
    
y = "y"
while y == "y":
    user1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6 ,7, 7, 8, 8, 9, 9, 10, 10, "A", "Q", "J", "K"]
    user2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6 ,7, 7, 8, 8, 9, 9, 10, 10, "A", "Q", "J", "K"]
    user1_cards = []
    user2_cards = []
    game = "c"
    start()
    while sum(user1_cards)<21 and sum(user2_cards)<21 and game == "c":
        print("""
                ╭────────────────────────────╮
                │        YOUR MOVE            │
                │                             │
                │   [H] Hit     [S] Stand     │
                ╰────────────────────────────╯
        """)
        choice = input("Enter you choice:")
        #User's turn
        if choice == "h":
            hit(user1)
            check_bust()
        elif choice == "s":
            stand()
        else:
            print("You entered wrong choice")
        #Dealer's Turn
        if game != "s":
            Dealer()
    else:
        check_bust()
    y = input("Do you want to continue or exit? press y to continue else press any other key.")



    