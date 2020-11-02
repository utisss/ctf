# Seccomp
* **Event:** SpookyCTF (ISSS CTF 10-28-2020)
* **Problem Type:** Binary Exploitation

## Background
[Netcat](https://en.wikipedia.org/wiki/Netcat) is an invaluable tool for testing networking and connecting to servers.

[Objdump](https://linux.die.net/man/1/objdump) Allows you to dump compiled code into readable assembly

[Pwntools](https://github.com/arthaud/python3-pwntools) is very useful when exploiting more complicated services.

[GDB](http://man7.org/linux/man-pages/man1/gdb.1.html) allows you to easily debug programs and see what is happening inside them at runtime.

[Seccomp](https://en.wikipedia.org/wiki/Seccomp) allows us to disable syscalls.

## Exploit
```
We have a buffer overflow, but can't call exec to get a shell.

Instead we need to call `open('/home/seccomp/flag', 0)`, `read(3, .bss, 100)`, `puts(.bss)`

We can do a really long ropchain to call these functions.

See the exploit script for more info.
```
