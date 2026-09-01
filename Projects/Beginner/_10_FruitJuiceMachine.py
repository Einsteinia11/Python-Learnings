from Data.FruitJuiceData import change_available, menu, ingredients, quantity_available
import time
#This code is for fruit juice machine
juice_type = ""
toppings = ""
cost = 0
flag = "True"
change = 0
user_cash = 1
user = {10: 0, 20: 0, 50: 0, 100: 0, 500: 0}
items_purchased = []
NOTE_ORDER = [500, 100, 50, 20, 10]

def check(type):
    #This function checks whether all the ingredients are available or not
    global juice_type
    global cost
    global flag
    juice_type = menu[type-1]

    print("Juice = ", juice_type)

    #Check availability
    for i, j in ingredients.items():
        for item, needed in j.items():
            if item == "price":
                if needed >= quantity_available.get(item, 0):
                    items_purchased.append({i: needed})
                continue
            else:
                print(quantity_available.get(item, 0))
                if needed > quantity_available.get(item, 0):
                    return False
                else:
                    recipe = j
                    for ing, count in recipe.items():
                        if ing == "price":
                            continue
                        else:
                            quantity_available[ing] -= needed
                    return True
     
def show_menu():
    count = 1
    for i in range(0, len(menu)):
        print(f"""
            {count} : {menu[i]}
        """)
        count+=1


def prepare_juice(choice):
    global flag
    global juice_type
    c = check(choice)
    print("c = ", c)
    if c == True:
        print("Everything's Good to go .", end = "", flush = True)
        # time.sleep(2)
        # print(".", end = "", flush=True)
        # time.sleep(3)
        # print(".")
        # print("Processing.", end = "", flush=True)
        # time.sleep(2)
        # print(".", end = "", flush=True)
        # time.sleep(3)
        # print(".")
        # print("Preparing🥤😋.", end = "", flush=True)
        # time.sleep(2)
        # print(".", end = "", flush=True)
        # time.sleep(3)
        print(".")
        print(f"Here's your {juice_type}")
        print("""
              \\
               \\
        ________\__
       /            \\
      /              \\
     | ~~~~~~~~~~~~~~ |
     | ~~~~~~~~~~~~~~ |
     | ~~~~ JUICE ~~~ |
     | ~~~~~~~~~~~~~~ |
      \              /
       \____________/
            ||
            ||
         ___||___
        """)


    elif c == False:
        print("Oops Sorry! There's not enough resources for the ordered item")
        flag = False

def calculate_savings():
    cash = 0
    for note, count in change_available.items():
        cash+=note*count
    return cash

def calculate_cost():
    global cost
    global change
    global items_purchased
    global user_cash
    global user
    print("cost = ",cost)
    cost = 0
    #Calculate total cost to be paid by user
    print("items_purchased = ", items_purchased)
    for k in items_purchased:
        for j in k.values():
            cost+=j


    print("Total cost = ", cost)
    while user_cash<cost:
        tens = int(input("Enter how many tens you have: "))
        twenty = int(input("Enter how many twenty you have: "))
        fifty = int(input("Enter how many fifty you have: "))
        hund = int(input("Enter how many hundreds you have: "))
        fhund = int(input("Enter how many five hundreds you have: "))
        #Calculate total cash user gave
        if tens>0:
            user_cash += tens*10
            user[10] = tens
        if twenty>0:
            user_cash += twenty*20
            user[20] = twenty
        if fifty>0:
            user_cash += fifty*50
            user[50] = fifty
        if hund>0:
            user_cash += hund*100
            user[100] = hund
        if fhund >0:
            user_cash += 500*fhund
            user[500] = fhund
        print("total cash you gave: ", user_cash)
        print(user)
        if user_cash<cost:
            print("Insufficient money please enter again")
    
    give_change()


def make_change(amount):
    """
    Try to build `amount` from the OWNER'S till (change_available),
    largest note first. Returns (True, breakdown) if possible,
    else (False, {}). Doesn't touch change_available -- caller commits it.
    """
    remaining = amount
    breakdown = {}
    for note in NOTE_ORDER:              # walk from biggest note to smallest
        available = change_available.get(note, 0)   # how many of THIS note do we have?
        if remaining <= 0 or available <= 0:
            continue                      # nothing more to do, or none of this note left
        take = min(remaining // note, available)
        #        ^^^^^^^^^^^^^^^^^^     ^^^^^^^^^
        #        "how many of this      "but don't take more
        #         note would fit into    than we actually have"
        #         what's left to pay?"
        if take > 0:
            breakdown[note] = take
            remaining -= take * note      # reduce what's still owed
    if remaining == 0:
        return True, breakdown
    return False, {}


def check_change():
    global user_cash
    global cost
    global user
    global change_available

    if user_cash == cost:
        return f"Thank You! We received a payment of Rs {cost}", {}

    if user_cash < cost:
        return "Insufficient money. Please pay the full amount.", {}

    change_due = user_cash - cost

    # Try 1: can the CUSTOMER's own notes cover `cost` exactly, leaving
    # the rest as change? If so, the owner's till never needs to move.
    kept = {}
    remaining = cost
    leftover = dict(user)  # scratch copy -- don't touch the real `user` dict yet

    for note in NOTE_ORDER:
        available = leftover.get(note, 0)
        if remaining <= 0 or available <= 0:
            continue
        take = min(remaining // note, available)
        if take > 0:
            kept[note] = take
            leftover[note] -= take
            remaining -= take * note

    if remaining == 0:
        returned = {note: count for note, count in leftover.items() if count > 0}
        for note, count in kept.items():
            change_available[note] = change_available.get(note, 0) + count
        return f"Thank you! Here is your change: {returned}", returned

    # Try 2: customer's notes didn't split evenly -- fall back to the
    # owner's separate till.
    savings = calculate_savings()
    if savings < change_due:
        return "Insufficient Change! Your money is refunded. Please pay the exact amount.", {}

    possible, breakdown = make_change(change_due)
    if not possible:
        return "Insufficient Change! Your money is refunded. Please pay the exact amount.", {}

    for note, count in user.items():
        change_available[note] = change_available.get(note, 0) + count
    for note, count in breakdown.items():
        change_available[note] -= count

    return f"Thank you! Here is your change: {breakdown}", breakdown
        
def give_change():
    message, change_breakdown = check_change()
    print(message)

c  = "y"
while c == "y":
    show_menu()
    choice = int(input("Enter choice: "))
    prepare_juice(choice)
    y = input("Enter y to show menu else press any other key to show bill: ")
    c = y
    if c != "y":
        calculate_cost()
    else:
        print("That's greak let's have one more juicy flavour to stay active all the day!")