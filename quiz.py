quizes = [
    {
        'quiz': 'What is the capital of france? ',
        'options': ['A. Paris', 'B. London', 'C. Berlin', 'D.Madrid'],
        'Answer': 'A'
    },
    {
        'quiz': 'Which language is primary speak in barzil?  ',
        'options': ['A. spanish', 'B. portugal', 'C. english', 'D. french'],
        'Answer': 'B'
    },
    {
        'quiz': 'What is the smallest prime number? ',
        'options': ['A. 1', 'B. 2', 'C. 3', 'D. 5'],
        'Answer': 'B'
    },
    {
        'quiz': 'who is me ? ',
        'options': ['A. hansa', 'B. dana', 'C. malith', 'D. givva'],
        'Answer': 'A'
    }

]


def run_quiz(quizes):
    score = 0
    for q in quizes:

        print(q['quiz'])
        for option in q['options']:
            print(option)
        answer = input('Enter your answer (A, B, C, D): ').upper()
        if answer != q['Answer']:
            print(f'Wrong! The correct answer is {q["Answer"]}')
        elif answer == q['Answer']:
            print('Your answer is correct')
            score += 1
        print('\n')

    print(f'You got {score} out of {len(quizes)} questions correct')


run_quiz(quizes)
