import random

computer_choises = ["r", "p", "s"]
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}


def get_user_choice():
    while True:
        your_choice = str(input('Rock, Paper, or scissor? (r/p/s): ')).lower()

        if your_choice in computer_choises:
            return your_choice

        else:
            print('Invalid choice!')


def display_choices(your_choice, computer_chose):
    print(f"your coice: {emojis[your_choice]}")
    print(f"computer choice: {emojis[computer_chose]}")


def get_winner(your_choice, computer_chose):
    if your_choice == computer_chose:
        print("You tie!")
    elif (
        (your_choice == 'r' and computer_chose == 's') or
        (your_choice == 's' and computer_chose == 'p') or
            (your_choice == 'p' and computer_chose == 'r')):
        print('you win')
    else:
        print('You lose')


def play_game():
    while True:
        your_choice = get_user_choice()

        computer_chose = random.choice(computer_choises)

        display_choices(your_choice, computer_chose)

        get_winner(your_choice, computer_chose)

        should_continue = str(input('Continue? (y/n): ')).lower()
        if should_continue == 'n':
            break


play_game()
