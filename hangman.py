import random

words = ['python', 'java', 'javascript', 'machine', 'rust']

computer_chose = random.choice(words)
word_display = ['_' for _ in computer_chose]
attempts = 8

print('Welcome to hungman!')

while attempts > 0 and '_' in word_display:
    print('\n' + ' '.join(word_display))
    guess = input('Guess a letter: ').lower()
    if guess in computer_chose:
        for index, letter in enumerate(computer_chose):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter dosen't appear in the word,  idiot !!! ")
        attempts -= 1

if '_' not in word_display:
    print("YOU GUESSED THE WORD")
    print(''.join(word_display))
    print('You survived')

else:
    print(f"You ran out attempts , The word was :{computer_chose}")
    print("You lost !")
