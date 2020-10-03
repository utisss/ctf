# Overflow
* **Event:** AmongUsCTF (ISSS CTF 10-02-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Exploit
```
Normal buffer overflow exploit. Since there is no "get_flag" function, we need to call system('/bin/sh').

Luckily I left the string "/bin/sh" and a call to system() in the code.
```
