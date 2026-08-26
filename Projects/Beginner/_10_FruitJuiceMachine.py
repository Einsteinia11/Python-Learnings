from Data.FruitJuiceData import change_available, menu, ingredients, quantity_available
import time
#This code is for fruit juice machine
juice_type = ""
toppings = ""
cost = 0
flag = "True"
change = 0
user_cash = 1
items_purchased = []
def check(type):
    #This function checks whether all the ingredients are available or not
    global juice_type
    global cost
    global flag
    for i in menu:
        if type == 1:
            juice_type = "Mango Juice"
            break
        elif type == 2:
            juice_type = "Apple Juice"
            break
        elif type == 3:
            juice_type = "Banana Juice"
            break
        elif type == 4:
            juice_type = "Pineapple Juice"
            break
        elif type == 5:
            juice_type = "Watermelon Juice"
            break
        elif type == 6:
            juice_type = "Banana Milkshake"
            break
        else:
            print("Invalid Number received!")
            break
    print("Juice = ", juice_type)
    for i, k in ingredients.items():
        print(k["price"])
        print(i)
        if i == juice_type:
            for j, h in quantity_available.items():
                fruitjuice= juice_type.split()
                fruit = fruitjuice[0]
                fruit = "".join(fruit)
                print("i = ", i, "k = ",k, "j = ", j, " h = ",h)
                if (juice_type == "Banana Juice" or juice_type == "Banana Milkshake") and j == "liquid_items":
                    if k["milk"] > h["milk"] or k["water"] > h["water"]:
                        print("less")
                        return 101
                    else:
                        print("more")
                        items_purchased.append({juice_type: k['price']})
                        return 103
                        
                elif j == "fruits":
                    if  k[fruit] > h[fruit]:
                        print("less1")
                        return 101
                    else:
                        print("more2")
                        items_purchased({juice_type: k['price']})
                        return 103
                if j == "liquid_items":
                    if k["water"] > h["water"]:
                        print("less3")
                        return 101
                    else:
                        items_purchased({juice_type: k['price']})
                        return 103
                    
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
    if c == 103:
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


    elif c == 101:
        print("Oops Sorry! There's not enough resources for the ordered item")
        flag = False

def calculate_cost():
    global cost
    global change
    global items_purchased
    global user_cash
    #Calculate total cost to be paid by user
    print("items_purchased = ", items_purchased)
    for k in items_purchased:
        for i, j in k.items():
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
        if twenty>0:
            user_cash += twenty*20
        if fifty>0:
            user_cash += fifty*50
        if hund>0:
            user_cash += hund*100
        if fhund >0:
            user_cash += 500*fhund
        print("total cash you gave: ", user_cash)
        if user_cash<cost:
            print("Insufficient money please enter again")
    
    give_change(tens, twenty, fifty, hund, fhund)

def check_change():
    global user_cash
    global cost
    c = 0
    if user_cash>cost:
        for i, j in change_available.items():
            if c+j <= cost:
                c+=j
                if c == cost:
                    break
            print("##i = ", i, "j = ", j)
    print(c)
    if c!=cost:
        print("Insufficient Change your money is refunded! Please enter the correct amount")

        

def give_change(tens = 0, twenty = 0, fifty = 0, hund = 0, fhund = 0):
    global change
    global cost
    global user_cash

    check_change()
    #Give change from saving
    # for i, j in change_available.items():
    #     print("i = ", i, "j = ", j)
    # c = 0
    
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