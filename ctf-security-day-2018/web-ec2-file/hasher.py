# -*- coding: utf-8 -*-
import hashlib
from cryptography.fernet import Fernet

m = hashlib.md5()
key = Fernet.generate_key()
cipher_suite = Fernet(key)
file = open("securityday.pem", "r")
data = cipher_suite.encrypt(file.read())
data =  "18.188.119.8" + "😠" + key + "😠" + data
m.update("securityday.pem")
f=open(m.hexdigest(), "w+")
f.write(data)
