import sys
import binascii

length = 4384
message = open("key.txt", 'r')
key = open("key2.txt", 'r')

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

print ''.join(chr(int(key2[i:i+8], 2)) for i in xrange(0, len(key2), 8))
