import hashlib
from cryptography.fernet import Fernet

m = hashlib.md5()
file = open("5112e7af5b5ce11f2e5f56649ed95277", "r")
all_data = file.read()
key = all_data.split("%")[0]
cipher_suite = Fernet(key)
data = cipher_suite.decrypt(all_data[len(key) + 1:])
final_file = open("test.jpg", "w")
final_file.write(data)
