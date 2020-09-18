# Overflow
* **Event:** IntroCTF (ISSS CTF 09-04-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Exploit
```
The buffer and x are allocated next to each other in memory. If we overflow buffer, we can overwrite x.

The buffer begins at rbp-0x70 and x is at rbp-4. If we fill the buffer with ``b'a'*(0x70-0x4) + b'\x37\x13\x00\x00'``, we will get a shell.
```
