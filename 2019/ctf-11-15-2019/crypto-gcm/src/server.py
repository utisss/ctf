from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from secret import flag

KEY = get_random_bytes(1)*16
IV = get_random_bytes(1)*16

def aes_gcm_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    return cipher.encrypt(plaintext)

def aes_gcm_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    return cipher.decrypt(ciphertext)

if __name__ == '__main__':
    print("I am so thankful for AES! Here's the flag:")
    print(aes_gcm_encrypt(flag, KEY, IV).hex())

