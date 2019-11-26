import base64, random
from Crypto.Cipher import AES

def aes_gcm_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    return cipher.decrypt(ciphertext)

s_hex = '5ec90bd84b3f47ecfb71ebdab2b521df1a1b493406c1a36b4c508a181c7c9d12dc63b8'
s = bytes.fromhex(s_hex)

for c1 in range(256):
    for c2 in range(256):
        key = bytes([c1] * 16)
        iv = bytes([c2] * 16)
        candidate = aes_gcm_decrypt(s, key, iv)
        if b'utflag' in candidate:
            print(candidate)
