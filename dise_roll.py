import random

while True:

    # .lower()  -> mek methn kelwrt add kloth user mkk enter klth ek lower case letter ekk wenw
    dice = str(input("Roll the dice? (y/n):"))

    if dice == 'y' or dice == 'Y':
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f"{num1} , {num2}")

    elif dice == 'n' or dice == 'N':
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice")
