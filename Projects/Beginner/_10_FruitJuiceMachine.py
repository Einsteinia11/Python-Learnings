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
            user[50] = hund
        if fhund >0:
            user_cash += 500*fhund
            user[500] = fhund
        print("total cash you gave: ", user_cash)
        print(user)
        if user_cash<cost:
            print("Insufficient money please enter again")
    
    give_change()

def check_change():
    global user_cash
    global cost #cost req to be paid
    c = 0 #change
    savings = calculate_savings()
    print(savings)
    def check_user_cash():
        for i, j in user.items():
            if 
    if user_cash == cost:
        return f"ThankYou We recieved a payment of RS {cost}"
    elif user_cash > cost :
        if user_cash > savings:
            if cost < user_cash:
                pass
    if c!=cost:
        print("Insufficient Change your money is refunded! Please enter the correct amount")
        calculate_cost()
        

def give_change():
    global change
    global cost
    global user_cash

    check_change()
    
    print(
        f"""
            ╔══════════════════════════════════════════╗
            ║            🍹 FRESH JUICE BAR 🍹         ║
            ║              CUSTOMER BILL               ║
            ╠══════════════════════════════════════════╣
            ║                                          ║
            ║  Item                     Price           ║
            ║  ──────────────────────────────────────  ║
            ║  Mango Juice              ₹50             ║
            ║  Banana Milkshake         ₹70             ║
            ║                                          ║
            ║  ──────────────────────────────────────  ║
            ║  TOTAL                    ₹120            ║
            ║                                          ║
            ║  Cash Received            ₹200            ║
            ║  Change                   ₹80             ║
            ║                                          ║
            ╠══════════════════════════════════════════╣
            ║       Thank you! Visit us again! 🥭      ║
            ╚══════════════════════════════════════════╝
        """
    )

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