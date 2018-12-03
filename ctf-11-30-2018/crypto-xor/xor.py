
def xor(string, key):
    result = ""
    for i in range(len(string)):
        result += chr(ord(string[i]) ^ ord(key[i % len(key)]))
    return result

def encrypt(message, key):
    output = open('encrypted', 'w')
    output.write(xor(message, key))
    output.close()

def decrypt(message, key):
    encrypted = open('encrypted', 'r').read().rstrip('\n')
    output = open('decrypted', 'w')
    output.write(xor(encrypted, key))
    output.close()

message = "utflag{n0w_y0u_4r3_x0r13nted} Congratulations! XOR is a simple but common algorithm to obfuscate a message."
key = "xorissuperb"

assert len(key) == 11
assert key.isalnum()
assert "utflag" in message

encrypt(message, key)
decrypt(message, key)
