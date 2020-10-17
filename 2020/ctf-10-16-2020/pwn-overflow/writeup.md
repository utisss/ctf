# Overflow
* **Event:** IntroCTF (ISSS CTF 10-16-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

## Exploit
```
There's a struct on the stack that we're expected to overwrite using a buffer overflow.

By inspecting the assembly we see that the string starts at rbp-0x90 and the struct.x is at rbp-0x20.

If we write 0x70 bytes of garbage then 0x1337, we will get a shell.

See exploit.py for more info
```
