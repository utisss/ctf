from pwn import *
import string

def send_and_recv(s):
    r.readline()
    r.sendline(s)
    r.readline()
    return bytes.fromhex(r.recvuntil("\n")[:-1].decode())

r = remote('localhost', 9003)

# Read intro
r.readline()

# Chosen Plaintext Attack
# Byte at a Time ECB Decryption
block_size = 16
secret = ''
prev = ''

for block in range(100):
    for i in range(0, block_size):
        init = 'A' * (block_size - i - 1)
        #print(init)
        byte = send_and_recv(init)[block_size * block:block*block_size + block_size]
        d = {}
        for c in string.ascii_letters + string.digits + string.punctuation:
            payload =  ('A' * (block_size - i - 1)) + secret + c
            #print(payload)
            ciphertext = send_and_recv(payload)
            d[c] = ciphertext[block_size * block:block*block_size + block_size]

        stop = False
        for key in d.keys():
            if d[key] == byte:
                secret += key

        print('secret', secret)
    if len(prev) == len(secret):
        break

    prev = secret
