import random

print("""
                            ╔══════════════════════════════════════════╗
                            ║            ♠ BLACKJACK ♠                 ║
                            ║         THE 21 CARD GAME                 ║
                            ╚══════════════════════════════════════════╝
""")

# ── FIX 1: ONE SHARED DECK, NOT TWO SEPARATE ONES ────────────────────────
# Originally user1 and user2 were both decks AND player identifiers, so
# each "player" drew from their own private 24-card deck. That let both
# players draw duplicate cards. Now there's a single deck both draw from,
# like a real table.
def new_deck():
    deck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
            "A", "A", "A", "A", "Q", "Q", "Q", "Q", "J", "J", "J", "J",
            "K", "K", "K", "K"]
    random.shuffle(deck)
    return deck

user1_cards = []  # your hand (raw cards, e.g. [7, "A"])
user2_cards = []  # dealer's hand
game = "c"


# ── FIX 2: PROPER ACE HANDLING ───────────────────────────────────────────
# The original check() decided Ace = 1 or 11 once, at the moment it was
# drawn, and baked that number permanently into the hand. That breaks the
# moment you draw another card afterward (e.g. [10, "A"] = 21 correctly,
# but then hitting a 5 gave 26/bust instead of correctly dropping the Ace
# to 1 for a 16). Now hands store the RAW card ("A", "K", 7, ...) and we
# recompute the total from scratch every time with total(), downgrading
# Aces from 11 to 1 as many times as needed to avoid busting.
def card_value(card):
    if card in ("J", "Q", "K"):
        return 10
    if card == "A":
        return 11
    return card

def total(hand):
    t = sum(card_value(c) for c in hand)
    aces = hand.count("A")
    while t > 21 and aces:
        t -= 10
        aces -= 1
    return t


def start(deck):
    def set_cards(user):
        for i in range(0, 2):
            r = deck.pop()
            user.append(r)
    set_cards(user1_cards)
    set_cards(user2_cards)
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

            Your total: {total(user1_cards)}
    """)


def hit(hand, deck, is_dealer=False):
    r = deck.pop()
    hand.append(r)
    if not is_dealer:
        print(f"""
            You chose: HIT

            Dealing a card...

            You received: {r}

            Your Total: {total(hand)}
        """)
        print("Your cards: ", hand)
    else:
        print(f"Dealer hits and draws a {r}.")
    return r


# ── FIX 4: ONE SINGLE SOURCE OF TRUTH FOR WIN/LOSS/PUSH ─────────────────
# Originally win/loss messages were printed from three different places
# (check_bust(), stand(), and implicitly the main loop) with formatting
# that could disagree with each other (e.g. a hardcoded "20 vs 20" in the
# tie message regardless of actual totals). Now there is exactly one
# function that decides and prints the result.
def resolve(final=False):
    global game
    p, d = total(user1_cards), total(user2_cards)

    if p > 21 and d > 21:
        print(f"""
        ────────────────────────────────────────────
                        💥 DOUBLE BUST!
        ────────────────────────────────────────────
            Your total: {p}
            Dealer total: {d}
                     It's a PUSH.
        ────────────────────────────────────────────
        """)
        game = "s"
    elif p > 21:
        print(f"""
        ────────────────────────────────────────────
                        💥 BUST!
        ────────────────────────────────────────────
            Your total: {p}
            Dealer total: {d}
                      Dealer Wins!
        ────────────────────────────────────────────
        """)
        game = "s"
    elif d > 21:
        print(f"""
                ╔══════════════════════════════════════════╗
                ║              YOU WIN! 🎉                 ║
                ╚══════════════════════════════════════════╝
                Your total:   {p}
                Dealer total: {d}
                The house couldn't beat you!
        """)
        game = "s"
    elif final:
        if p > d:
            print(f"""
                ╔══════════════════════════════════════════╗
                ║              YOU WIN! 🎉                 ║
                ╚══════════════════════════════════════════╝
                Your total:   {p}
                Dealer total: {d}
            """)
        elif p < d:
            print(f"""
                ────────────────────────────────────────────
                                💥 You Lose!
                ────────────────────────────────────────────
                Your total: {p}
                Dealer total: {d}
                            DEALER WINS
                ────────────────────────────────────────────
            """)
        else:
            print(f"""
                ────────────────────────────────────────────
                                PUSH 🤝
                ────────────────────────────────────────────
                Your total:   {p}
                Dealer total: {d}
                It's a tie! Bet returned.
                ────────────────────────────────────────────
            """)
        game = "s"


def stand(deck):
    global game
    # ── FIX 3: DEALER FOLLOWS A FIXED RULE, NOT RANDOM CHOICE ───────────
    # Originally the dealer randomly picked hit/stand once between 17-21,
    # which isn't how blackjack dealers behave and made the dealer bust
    # itself for no reason. Now the dealer always hits under 17 and
    # always stands at 17+, which is the standard casino rule.
    while total(user2_cards) < 17:
        hit(user2_cards, deck, is_dealer=True)
    resolve(final=True)


def Dealer(deck):
    if total(user2_cards) < 17:
        hit(user2_cards, deck, is_dealer=True)
    # If dealer is >= 17, dealer takes no action on the player's turn;
    # it only finishes drawing once the player stands (see stand()).


y = "y"
while y == "y":
    deck = new_deck()
    user1_cards = []
    user2_cards = []
    game = "c"
    start(deck)

    while total(user1_cards) < 21 and total(user2_cards) < 21 and game == "c":
        print("""
                ╭────────────────────────────╮
                │        YOUR MOVE            │
                │                             │
                │   [H] Hit     [S] Stand     │
                ╰────────────────────────────╯
        """)
        choice = input("Enter you choice:").strip().lower()

        # ── FIX 5: BAD INPUT NO LONGER BURNS YOUR TURN ───────────────────
        # Originally an invalid choice still let the dealer take a turn
        # afterward, silently costing the player their move. Now an
        # invalid choice just re-prompts.
        if choice == "h":
            hit(user1_cards, deck)
            resolve()
        elif choice == "s":
            stand(deck)
        else:
            print("You entered wrong choice, try again.")
            continue

        if game != "s":
            Dealer(deck)
    else:
        resolve(final=True)

    y = input("Do you want to continue or exit? press y to continue else press any other key.")