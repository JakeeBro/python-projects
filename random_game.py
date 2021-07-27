import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])

if start < end:
    answer = randint(start, end)
else:
    print("Please Restart and Enter a Valid Number Range")
    sys.exit()


def game_loop():

    print(f'\nGuess a Number between {start} and {end}')
    guess = input()
    try:
        if int(guess) == answer:
            print("Correct!")
            return
        else:
            print('Try Again')
            game_loop()
    except ValueError:
        print('Please Enter a Number')
        game_loop()


game_loop()
