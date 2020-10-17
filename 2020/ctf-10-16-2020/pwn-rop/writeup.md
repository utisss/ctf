# ROP
* **Event:** TetrisCTF (ISSS CTF 10-16-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Buffer overflow](https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/) - Common binary exploitation technique

## Exploit
```
A buffer overflow is a common binary exploitation technique.

Our buffer is at rbp-0x210. If we fill the buffer with (512+16)*b'a' 0x1337 + addr_of_get_shell we'll get a shell.

See exploit.py for more info
```
