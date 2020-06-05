import random

print('''
Welcome to Rock, Paper, Scissors!!

You get to play this awesome game against a computer.

Please enter r for rock, p for paper, and s for scissors
''')

user_choice = input('Enter your choice here: ')

choices = ['s', 'p', 'r']

computer_choice = random.choice(choices)

if user_choice.lower() == 'p':
    if computer_choice == 'p':
        print('''
        It\'s a tie
        Computer chose paper.
        ''')
    elif computer_choice == 's':
        print('''
        Computer won!
        Computer chose scissors.
        ''')
    elif computer_choice == 'r':
        print('''
        You won!
        Computer chose rock.
        ''')
    else:
        print('Something went wrong')
elif user_choice.lower() == 's':
    if computer_choice == 's':
        print('It\'s a tie')
    elif computer_choice == 'r':
        print('Computer won!')
    elif computer_choice == 'p':
        print('You won!')
    else:
        print('Something went wrong')
elif user_choice.lower() == 'r':
    if computer_choice == 'r':
        print('It\'s a tie')
    elif computer_choice == 'p':
        print('Computer won!')
    elif computer_choice == 's':
        print('You won!')
    else:
        print('Something went wrong')
else:
    print('Something went wrong')