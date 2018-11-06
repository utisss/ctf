from passlib.hash import cisco_type7

f = open('flag.txt', 'r')
word = f.read().rstrip('\n')

h = cisco_type7.hash(word)
print(h)
