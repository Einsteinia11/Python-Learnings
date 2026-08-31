change_available = {
    10: 100,
    20: 20,
    50: 20,
    100: 12,
    500: 10
}

exit_codes = {
    101: "Oops Sorry! There's not enough resources for the ordered item.",
    102: "Oops Sorry! There's no change you need to give the exact amount!",
    103: "Everything's good to go."
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

# FLATTENED -- no more "liquid_items" / "fruits" nesting. juice_machine.py
# looks ingredients up directly by name (quantity_available.get("water", 0)),
# so nesting them under a sub-dict made every lookup silently fail and
# return 0, which is why every juice was being rejected.
#
# water bumped from 100 -> 1000: at 100, only the Banana items (50ml) could
# ever succeed, since every other juice needs 200ml. Adjust if you want
# different starting stock, just keep it a flat top-level key.
quantity_available = {
    "water": 1000,       # ml
    "milk": 5000,        # ml
    "Mango": 10,          # number of mangoes
    "Apple": 12,          # number of apples
    "Banana": 20,         # number of bananas
    "Pineapple": 5,       # number of pineapples
    "Watermelon": 4,      # number of watermelons
}