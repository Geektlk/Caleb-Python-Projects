import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Try again. Too low!.')
        elif guess > random_number:
            print('Sorry, Try again. Too high!.')
    print(f'Congrats u guessed {random_number} correctly')
guess(10)