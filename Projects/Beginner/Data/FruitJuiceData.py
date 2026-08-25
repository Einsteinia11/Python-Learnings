change_available = {
    10: 0,
    20: 0,
    50: 0,
    100: 0,
    200: 0,
    500: 0
}

exit_codes = {
    101: "",
    102: "Oops Sorry! There's no change you need to give the exact amount!",
    103: ""
}

menu = [
    "Mango Juice",
    "Apple Juice",
    "Banana Juice",
    "Pineapple Juice",
    "Watermelon Juice",
    "Banana Milkshake"
]

ingredients = {
    "Mango Juice": {
        "price": 50,
        "Mango": 2,
        "water": 200
    },
    "Apple Juice": {
        "price": 50,
        "Apple": 2,
        "water": 200
    },
    "Banana Juice": {
        "price": 40,
        "Banana": 2,
        "milk": 200,
        "water": 50
    },
    "Pineapple Juice": {
        "price": 60,
        "Pineapple": 2,
        "water": 200
    },
    "Watermelon Juice": {
        "price": 50,
        "Watermelon": 2,
        "water": 200
    },
    "Banana Milkshake": {
        "price": 70,
        "Banana": 2,
        "milk": 250,
        "water": 50
    }
}

quantity_available = {
    "liquid_items" : {
        "water": 100,        # ml
        "milk": 5000,         # ml  
    },
    "fruits":{
        "Mango": 10,          # number of mangoes
        "Apple": 12,          # number of apples
        "Banana": 20,         # number of bananas
        "Pineapple": 5,       # number of pineapples
        "Watermelon": 4,      # number of watermelons
    }
}