import random

"""subs = {}

remaining = [chr(i + 97) for i in range(0, 26)]
random.shuffle(remaining)

for i in range(0, 26):
	subs[chr(i + 97)] = remaining[i]

print subs"""

subs = {'a': 'i', 'c': 'h', 'b': 'p', 'e': 'a', 'd': 'u', 'g': 'd', 'f': 's', 'i': 'j', 'h': 'y', 'k': 'r', 'j': 'f', 'm': 'e', 'l': 'o', 'o': 'w', 'n': 'x', 'q': 'm', 'p': 'b', 's': 'k', 'r': 'n', 'u': 'v', 't': 't', 'w': 'l', 'v': 'q', 'y': 'g', 'x': 'c', 'z': 'z'}

ciphertext = "You know, the method of frequency analysis is a pretty common way to solve substitution code problems. It happens when you have a substitution code with a ton of text with representation of letters that kind of matches the frequencies that occur in the alphabet. You start by guessing commonly occuring vowels, and use those to infer other words and build up to other vowels. If you are lucky, you will find out that you get a flag crib_dragging_aint_something_to_crib_about and that might help a bit. If you got this far, congratulations! You have figured out the essence of deciphering substitution codes. Hopefully it was not too difficult!"


output = ""
for char in ciphertext:
	if ord(char) >= 97 and ord(char) <= 122:
		output += subs[char]
	else:
		output += char

print output