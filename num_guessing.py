import random
num = random.randint(1, 100)

while True:

    try:
        choice = int(input('Guessing the number between 1 and 100: '))
        if choice > num:
            print("Too high!")
        elif choice < num:
            print("Too low!")
        elif choice == num:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number")
