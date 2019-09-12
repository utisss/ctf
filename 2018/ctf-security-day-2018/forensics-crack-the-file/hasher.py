import hashlib
from cryptography.fernet import Fernet

m = hashlib.md5()
key = Fernet.generate_key()
cipher_suite = Fernet(key)
file = open("truedaddy.jpg", "r")
data = cipher_suite.encrypt(file.read())
data = key + "%"  + data
m.update("truedaddy.jpg")
f=open(m.hexdigest(), "w+")
f.write(data)
