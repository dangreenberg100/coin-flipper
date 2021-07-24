import random

active: bool = True
while active:
    print("Welcome to the coin flipper")
    print("---------------------------")
    value = random.randint(1, 2)
    if value == 1:
        print("You landed on Tails\n")
    if value == 2:
        print("You landed on Heads\n")
    statement = int(input("|If you would like to exit type 1 or type 0 to continue: \n"))  # shutdown statement
    if statement == 1:
        break
