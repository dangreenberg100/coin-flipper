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
    statement = input("Would you like to continue y or n: \n")  # shutdown statement
    finish = "n" or "N"
    if statement == finish:
        break
