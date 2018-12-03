def xor(string, key):
    result = ""
    for i in range(len(string)):
        result += chr(ord(string[i]) ^ ord(key[i % len(key)]))
    return result

def encrypt(message, key):
    output = open('encrypted', 'w')
    output.write(xor(message, key))
    output.close()

message = open('message', 'r').read()
key = open('key', 'r').read()

assert len(key) == 11
assert key.isalnum()
assert "utflag" in message

encrypt(message, key)
