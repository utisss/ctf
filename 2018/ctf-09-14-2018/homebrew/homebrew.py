#!/usr/bin/env python3
import base64
import subprocess
import hashlib

password = "69asper420"

commands = ["ls", "cat", "echo", "help"]

def encrypt(msg):
    ciphertext = ''
    m = hashlib.md5()
    m.update(msg.encode())
    msg = msg + ' ' + m.hexdigest()
    for idx, char in enumerate(msg):
        ciphertext += chr((ord(char) ^ ord(password[idx % len(password)])))
    return base64.b64encode(ciphertext.encode()).decode("utf-8")

def verify(msg):
    try:
        msg = base64.b64decode(msg).decode("utf-8")
    except:
        print("Invalid command...exiting")
        exit()
    command = ''
    for idx, char in enumerate(msg):
        command += chr((ord(char) ^ ord(password[idx % len(password)])))

    syntax = command.split(" ")
    if(syntax[0] in commands):
        m = hashlib.md5()
        for idx, word in enumerate(syntax[:-2]):
            m.update((word+' ').encode())
        m.update(syntax[-2].encode())
        if(m.hexdigest() == syntax[-1]):
            subprocess.call(syntax[:-1])
        return True
    else:
        print("Invalid command...exiting")
        exit()
        return False


# print(encrypt("ls"))
# print(encrypt("cat assignment.txt"))

while (True):
    command = input("$ ")
    verify(command)

