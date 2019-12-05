import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

newLower = ''.join(random.sample(lower, len(lower)))
newUpper = ''.join(random.sample(upper, len(upper)))

plain = open('plain.txt', 'r').read()
#plain = input('Input the string you would like to encode: ')
cipher = ''

for letter in plain:
    print(letter)
    if letter in lower:
        cipher += newLower[lower.index(letter)]
    elif letter in upper:
        cipher += newUpper[upper.index(letter)]
    else:
        cipher += letter

print(cipher)
