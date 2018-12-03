from itertools import product

def xor(string, key):
    result = ""
    for i in range(len(string)):
        result += chr(ord(string[i]) ^ ord(key[i % len(key)]))
    return result

message = open('encrypted', 'r').read()
possibles = [''.join(x) for x in product('qwertyuiopasdfghjklzxcvbnm01234567890', repeat=3)]
for thing in possibles:
    res = xor(message, 'xorissu' + thing + 'b')
    works = True
    for yes in res:
        if yes not in '!qwertyuiopasdfghjklzxcvbnm{}_1234567890 ':
            works = False
    print(res)
    if works:
        print(res)

possibles = [''.join(x) for x in product('qwertyuiopasdfghjklzxcvbnm0123456789', repeat=1)]

"""print(possibles)
start = 'utflag{'
res = ""
for i in range(len(start)):
    print(i)
    for test in possibles:
        if xor(test, message[i]) == start[i]:
            print(res)
            res += test
print(res)"""
