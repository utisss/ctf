import sys
import binascii

length = 4384
message = open("flag.txt", 'r')
key = open("key.txt", 'r')

key = key.read()[:length]
message = message.read()[:length]

key2 = ""
for i in range(length):
    messageChar = message[i]
    keyChar = key[i]
    if messageChar == '0' and keyChar == '0':
        key2 += '0'
    elif messageChar == '0' and keyChar == '1':
        key2 += '1'
    elif messageChar == '1' and keyChar == '0':
        key2 += '1'
    elif messageChar == '1' and keyChar == '1':
        key2 += '0'
    else:
        print messageChar + ' ' + keyChar
        print "jiggy"


output = open('key2.txt', 'w')
output.write(key2)
output.close()

