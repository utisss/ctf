from secrets import key
data = open('plaintext.txt', 'r').readline()
ciphertext = open('ciphertext.txt', 'w')
encrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
ciphertext.write(encrypted)


