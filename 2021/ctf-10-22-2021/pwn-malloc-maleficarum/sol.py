#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './tristan'

e = ELF('./tristan')
rop = ROP('./tristan')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5000)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./tristan', cwd='problemDir')
else:
    p = e.process()

p.interactive()
