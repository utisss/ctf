import random

"""subs = {}

remaining = [chr(i + 97) for i in range(0, 26)]
random.shuffle(remaining)

for i in range(0, 26):
	subs[chr(i + 97)] = remaining[i]

print subs"""

subs = {'a': 'i', 'c': 'h', 'b': 'p', 'e': 'a', 'd': 'u', 'g': 'd', 'f': 's', 'i': 'j', 'h': 'y', 'k': 'r', 'j': 'f', 'm': 'e', 'l': 'o', 'o': 'w', 'n': 'x', 'q': 'm', 'p': 'b', 's': 'k', 'r': 'n', 'u': 'v', 't': 't', 'w': 'l', 'v': 'q', 'y': 'g', 'x': 'c', 'z': 'z'}

ciphertext = "congratulations! you have finished the beginner cryptography challenge. here is a flag for all your hard efforts: utflag{fancy_encodings_make_great_crypto}. you will find that a lot of cryptography is just building off this sort of basic knowledge, and it really is not so bad after all. hope you enjoyed the challenge!"


output = ""
for char in ciphertext:
	if ord(char) >= 97 and ord(char) <= 122:
		output += subs[char]
	else:
		output += char

print output
