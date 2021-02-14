from pwn import *

p = remote('localhost',9001)
with open('sol','rb') as file:
    stuff = file.read()
    print(str(len(stuff)))
    p.send(stuff)
    #p.shutdown('send')
    p.stream()
