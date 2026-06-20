import random

computer_choises = ["r", "p", "s"]
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}


while True:
    your_choice = str(input('Rock, Paper, or scissor? (r/p/s): ')).lower()

    if your_choice not in computer_choises:
        print('Invalid choice!')
        continue

    computer_chose = random.choice(computer_choises)

    print(f"your coice: {emojis[your_choice]}")
    print(f"computer choice: {emojis[computer_chose]}")

    if your_choice == computer_chose:
        print("You tie!")
    elif (
        (your_choice == 'r' and computer_chose == 's') or
        (your_choice == 's' and computer_chose == 'p') or
            (your_choice == 'p' and computer_chose == 'r')):
        print('you win')
    else:
        print('You lose')

    should_continue = str(input('Continue? (y/n): ')).lower()
    if should_continue == 'n':
        break
