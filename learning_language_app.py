import random


words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": ["of", "from"]},
    {"spanish": "que", "english": "that/which"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to/at"},
    {"spanish": "en", "english": "in/on"},
    {"spanish": "un", "english": "a/an"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself/itself"},
    {"spanish": "no", "english": "no/not"},
    {"spanish": "haber", "english": "to have (auxiliary)"},
    {"spanish": "por", "english": "for/by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/your/their"},
    {"spanish": "para", "english": "for/to"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "him/her/you (indirect object)"},
    {"spanish": "lo", "english": "it/him/you (direct object)"}
]


def quiz_user(words):
    computer_chose = random.shuffle(words)
    score = 0
    for word in words:
        print(f"What is the English translation of '{word['spanish']}'")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == word['english']:
            print("Your answer is correct. ")
            score += 1
        else:
            print(
                f"Your answer is incorrect idiot!! , Correct answer is '{word['english']}'")
    print(f"Your score is {score} out of {len(words)} ")


def main():
    print("Welcome to the Language Learning Flashcard App!")
    input("Please Enter to start the quiz ...")
    quiz_user(words)


if __name__ == "__main__":
    main()
