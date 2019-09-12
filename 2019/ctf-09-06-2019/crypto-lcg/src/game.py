from secrets import a, c, flag
import time

# TODO: Move this value to secrets.py eventually
m = 1 << 64


def lcg(a, c, modulus, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


# Initialize random number generator
rand = lcg(a, c, m, int(time.time()))
print("Can you guess the next number?")

while True:
    print("Guess a number (enter 'q' to quit):", end=' ')
    guess = input()
    if guess == 'q':
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Enter a positive number!")
        continue

    val = next(rand)

    if guess == val:
        print("Impossible!", flag)
        break

    print("Wrong guess, correct value was:", val)
