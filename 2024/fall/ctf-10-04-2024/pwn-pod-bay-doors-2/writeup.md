# Bepis
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

## Exploit
```
Passing user input directly into printf without printing %s, input lets the user make their own printf
format specifiers in the string. We simply spam %016lx to read the upper part of the stack and find 
the flag there eventually.
```
