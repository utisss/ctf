# -*- coding: utf-8 -*-
import hashlib
from cryptography.fernet import Fernet

m = hashlib.md5()
file = open("15abff565e0f7e7fdfffec64032f7655", "r")
all_data = file.read()
key = all_data.split("😠")[1]
ip = all_data.split("😠")[1]
print(ip)
cipher_suite = Fernet(key)
data = cipher_suite.decrypt(all_data[len(key) + len("😠") + len(all_data.split("😠")[0]):])
final_file = open("test.pem", "w")
final_file.write(data)
