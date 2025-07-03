import random

# This is where all our functions and variables will go.
#user input for storage: user will enter the activity they want to do.
userinput = input("What do you want to do? (help for list of activities and commands.)")

def parseinput(userinput):
    if userinput = 'help':
        print("------AVAILABLE COMMANDS: ------ \n roll : roll for an item.")
    elif userinput = "roll":
        roll()
    else:
        print("Unknown command")
        print("please enter the activity you want to do! (Help for list)")

# Mapping rollable items to numbers
items= ["diamond", "jam", "ruby"]

def roll():
    item = random.choice(items)
    print(f"you rolled a {item}!")
    return item
