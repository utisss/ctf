# Int
* **Event:** IntroCTF (ISSS CTF 09-04-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Exploit
```
Since i is a uint8_t, it must be between [-128,127]. If we keep adding 1, we'll wrap from 127 to -128. Eventually we'll hit -1 and get a shell.

See exploit.py
```
