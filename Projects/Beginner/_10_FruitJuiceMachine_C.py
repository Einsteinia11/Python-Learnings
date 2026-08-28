from Data.FruitJuiceData import change_available, exit_codes, menu, ingredients, quantity_available

# This code is for the fruit juice machine
items_purchased = []  # list of {juice_name: price} dicts, one per item bought

# Denominations only ever change if you edit FruitJuiceData.py, so there's no
# need to sort() them at runtime -- just declare the order once, largest first.
NOTE_ORDER = [500, 100, 50, 20, 10]

JUICE_ART = """
              \\
               \\
        ________\\__
       /            \\
      /              \\
     | ~~~~~~~~~~~~~~ |
     | ~~~~~~~~~~~~~~ |
     | ~~~~ JUICE ~~~ |
     | ~~~~~~~~~~~~~~ |
      \\              /
       \\____________/
            ||
            ||
         ___||___
"""


def show_menu():
    for i, name in enumerate(menu, start=1):
        print(f"\n            {i} : {name}\n")


def check_and_reserve(juice_name):
    """
    Check every ingredient the recipe needs (not just the first one found).
    If everything is in stock, deduct it from quantity_available and return
    True. If anything is short, deduct nothing and return False.
    """
    recipe = ingredients[juice_name]

    for ingredient, needed in recipe.items():
        if ingredient == "price":
            continue
        if needed > quantity_available.get(ingredient, 0):
            return False  # nothing has been deducted yet -- safe to bail out

    for ingredient, needed in recipe.items():
        if ingredient == "price":
            continue
        quantity_available[ingredient] -= needed

    return True


def prepare_juice(choice):
    if not (1 <= choice <= len(menu)):
        print("Invalid Number received!")
        return

    juice_name = menu[choice - 1]

    if check_and_reserve(juice_name):
        items_purchased.append({juice_name: ingredients[juice_name]["price"]})
        print(f"{exit_codes[103]} Here's your {juice_name}!")
        print(JUICE_ART)
    else:
        print(exit_codes[101])


def calculate_cost():
    """Fresh sum every time -- never accumulates across calls."""
    return sum(price for item in items_purchased for price in item.values())


def calculate_savings():
    return sum(note * count for note, count in change_available.items())


def make_change(amount):
    """
    Greedy, largest-note-first. Returns (True, breakdown) if `amount` can be
    built exactly from change_available, else (False, {}). Does not mutate
    change_available -- caller commits the result once confirmed.
    """
    remaining = amount
    breakdown = {}

    for note in NOTE_ORDER:
        available = change_available[note]
        if remaining <= 0 or available <= 0:
            continue
        notes_used = min(remaining // note, available)
        if notes_used > 0:
            breakdown[note] = notes_used
            remaining -= notes_used * note

    if remaining == 0:
        return True, breakdown
    return False, {}


def collect_payment(cost):
    """
    Repeatedly asks for notes until the customer has paid enough.
    Returns (total_cash_given, notes_given) without touching change_available
    yet -- we only commit the payment once we know we CAN give change for it.
    """
    user_cash = 0
    notes_given = {note: 0 for note in change_available}

    while user_cash < cost:
        print(f"\nTotal to pay: ₹{cost}  |  Given so far: ₹{user_cash}")
        for note in NOTE_ORDER:
            count = int(input(f"Enter how many ₹{note} notes you have: "))
            notes_given[note] += count
            user_cash += note * count
        if user_cash < cost:
            print(f"Insufficient money (₹{user_cash} given). Please add more.\n")

    return user_cash, notes_given


def print_bill(cost, paid, change_due, breakdown):
    item_lines = "\n".join(
        f"            {name:<22}₹{price}"
        for item in items_purchased
        for name, price in item.items()
    )
    change_lines = ", ".join(f"{c}x₹{n}" for n, c in breakdown.items()) or "—"

    print(f"""
            ╔══════════════════════════════════════════╗
            ║            🍹 FRESH JUICE BAR 🍹          ║
            ║              CUSTOMER BILL                ║
            ╠══════════════════════════════════════════╣
{item_lines}
            ──────────────────────────────────────────
            TOTAL                  ₹{cost}
            Cash Received          ₹{paid}
            Change                 ₹{change_due}  ({change_lines})
            ╠══════════════════════════════════════════╣
            ║       Thank you! Visit us again! 🥭       ║
            ╚══════════════════════════════════════════╝
    """)


def checkout():
    cost = calculate_cost()
    if cost == 0:
        print("No items purchased yet.")
        return

    user_cash, notes_given = collect_payment(cost)
    change_due = user_cash - cost

    if change_due == 0:
        for note, count in notes_given.items():
            change_available[note] += count
        print_bill(cost, user_cash, 0, {})
        items_purchased.clear()
        return

    # Only commit the payment to the till once we've confirmed we can make change
    if calculate_savings() < change_due:
        print(exit_codes[102])
        print("No cash has been taken. Please try again with the exact amount.")
        return

    possible, breakdown = make_change(change_due)
    if not possible:
        print(exit_codes[102])
        print("No cash has been taken. Please try again with the exact amount.")
        return

    for note, count in notes_given.items():
        change_available[note] += count
    for note, count in breakdown.items():
        change_available[note] -= count

    print_bill(cost, user_cash, change_due, breakdown)
    items_purchased.clear()


def main():
    while True:
        show_menu()
        raw = input("Enter choice: ").strip()
        if not raw.isdigit():
            print("Please enter a number.")
            continue

        prepare_juice(int(raw))

        again = input("Enter y to order another juice, else press any other key to checkout: ").strip().lower()
        if again != "y":
            break
        print("That's great, let's have one more juicy flavour to stay active all day!")

    checkout()


if __name__ == "__main__":
    main()