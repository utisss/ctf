from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64decode


raw_cipher_data = "utflag{m@ybedontusesomanykeys}"

for i in range(0,20):
    cipher = RSA.importKey(open('public_keys/key'+str(i)+'.pem', "rb").read())
    raw_cipher_data = cipher.encrypt(raw_cipher_data, 0)
    raw_cipher_data = raw_cipher_data[0]
    print i


out = open("encrypted", "wb")

out.write(raw_cipher_data)
