from secret import flag

for x in flag:
    print(chr(ord(x) + 0x1F500), end='')
