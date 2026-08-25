from Data.FruitJuiceData import change_available, menu, ingredients, quantity_available

#This code is for fruit juice machine
juice_type = ""
toppings = ""
cost = ""
flag = "True"
change = 0
items_purchased = []
def check(type):
    #This function checks whether all the ingredients are available or not
    global juice_type
    global cost
    global flag
    for i in menu:
        if type == 1:
            juice_type = "Mango Juice"
            items_purchased.append(juice_type)
        elif type == 2:
            juice_type = "Apple Juice"
            items_purchased.append(juice_type)
        elif type == 3:
            juice_type = "Banana Juice"
            items_purchased.append(juice_type)
        elif type == 4:
            juice_type = "Pineapple Juice"
            items_purchased.append(juice_type)
        elif type == 5:
            juice_type = "Watermelon Juice"
            items_purchased.append(juice_type)
        elif type == 6:
            juice_type = "Banana Milkshake"
            items_purchased.append(juice_type)
        else:
            print("Invalid Number received!")
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
                        return 103
                        
                elif j == "fruits":
                    if  k[fruit] > h[fruit]:
                        print("less1")
                        return 101
                    else:
                        print("more2")
                        return 103
                if j == "liquid_items":
                    if k["water"] > h["water"]:
                        print("less3")
                        return 101
                    else:
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
    c = check(choice)
    print("c = ", c)
    if c == 103:
        print("Everything's Good to go ...")
        print("Processing ...")

    elif c == 101:
        print("Oops Sorry! There's not enough resources for the ordered item")
        flag = False



def calculate_cost():
    pass

def give_change(tcost = 0,tens = 0, twenty = 0, fifty = 0, hund = 0, thund = 0, fhund = 0):
    global change
    c = 0
    user_cash = []
    while c!= tcost:
        if tcost or tens or twenty or fifty or hund or thund or fhund:
            while tens>0:
                user_cash.append(10)
                tens-=1
            while twenty>0:
                user_cash.append(20)
                twenty-=1
            while fifty>0:
                user_cash.append(50)
                fifty-=1
            while hund>0:
                user_cash.append(100)
                hund-=1
            while thund>0:
                user_cash.append(200)
                thund-=1
            while fhund>0:
                user_cash.append(500)
                fhund-=1
        for i in range(0, len(user_cash)):
            pass
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

show_menu()
choice = int(input("Enter choice: "))
prepare_juice(choice)

