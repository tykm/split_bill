food = {
    "Tyler": {
        "Spicy Rigatoni": 24,
    },
    "Anuraag": {
        "Chocolate Milkshake": 8.50,
        "Veggie Burger": 19.75,
    },
    "Kevin": {
        "Guiness": 8,
        "Buffalo Chicken Sandwich": 19,
    },
    "Jay": {
        "Doctors Orders": 15,
        "Oreo Milkshake": 9.50,
        "Penne Alla Vodka": 24,
    },
    "Patricia": {
        "Gin": 18,
        "Shrimp Pasta": 28,
    },
    "Katie": {
        "Secret Garden": 15,
        "Chocolate Milkshake": 8.50,
        "Chicken Parm": 24,
    },
}

shared = {
    "Truffle Fries": 12,
    "Non Cash Adjustment": 9.33
}

shared_per_person = sum(shared.values()) / len(food)
tax_multiplier = 1.06625
tip_multipler = 1.2
subtotal = 242.58
taxtotal = 258.15
tiptotal = 309.77

running_total = 0
for person in food:
    cost = sum(food[person].values()) + shared_per_person
    cost *= tax_multiplier
    cost *= tip_multipler
    cost = round(cost, 2)
    print(person + ": " + str(cost))
    running_total += cost

print(running_total)
