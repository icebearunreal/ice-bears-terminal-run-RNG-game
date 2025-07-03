import random

# This is where all our functions and variables will go.

# Mapping rollable items to numbers
items= ["diamond", "jam", "ruby"]

def roll():
    item = random.choice(items)
    print(f"you rolled a {item}!")
    return item
