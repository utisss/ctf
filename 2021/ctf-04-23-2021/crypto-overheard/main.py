from secret import msg
import os

assert "North Macedonia" in msg
assert "Wales" in msg

key_len = 10
key = os.urandom(key_len)
enc = []
for i in range(len(msg)):
    enc += [ord(msg[i]) ^ key[i % key_len]]

print(bytes(enc))
